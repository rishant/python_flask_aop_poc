import importlib
import pkgutil
import services

method_registry = {}


def method_mapper(name):
    def decorator(func):
        func._method_name = name
        return func

    return decorator


class BaseService:
    def __init__(self):
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr) and hasattr(attr, '_method_name'):
                method_registry[attr._method_name] = attr


# Dynamically load and register methods from all service modules in the `services` package
for _, module_name, _ in pkgutil.iter_modules(services.__path__):
    module = importlib.import_module(f"services.{module_name}")
    service_class_name = ''.join(
        [part.capitalize() for part in module_name.split('_')])  # Convert module_name to CamelCase
    service_class = getattr(module, service_class_name)
    service_instance = service_class()  # Create an instance of the service class
    # Register methods from the instance
    for attr_name in dir(service_instance):
        attr = getattr(service_instance, attr_name)
        if callable(attr) and hasattr(attr, '_method_name'):
            method_registry[attr._method_name] = attr


def handle_request(json_request):
    method_name = json_request.get('method')
    params = json_request.get('params', {})

    if method_name in method_registry:
        method = method_registry[method_name]
        return method(params)
    else:
        return {"error": "Method not found"}
