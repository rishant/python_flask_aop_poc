from service_registry import BaseService, method_mapper


class ExternalService(BaseService):

    @method_mapper('external_api_call')
    def external_api_action(self, param):
        # print(f"Performing External api call action with param: {param}")
        return {"status": "external_api_success", "param": param}
