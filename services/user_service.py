from service_registry import BaseService, method_mapper


class UserService(BaseService):

    @method_mapper('user_create')
    def user_create_action(self, param):
        # print(f"Performing create action with param: {param}")
        return {"status": "user_create_success", "param": param}

    @method_mapper('user_delete')
    def user_delete_action(self, param):
        # print(f"Performing delete action with param: {param}")
        return {"status": "user_delete_success", "param": param}
