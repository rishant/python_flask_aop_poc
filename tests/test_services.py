import unittest
from service_registry import handle_request


class TestServices(unittest.TestCase):

    def test_user_service(self):
        request = {
            "method": "user_create",
            "params": {"param": "test_user_create"}
        }
        response = handle_request(request)
        self.assertIn('user_create_success', response['status'])

    def test_external_service(self):
        request = {
            "method": "external_api_call",
            "params": {"param": "test_external"}
        }
        response = handle_request(request)
        self.assertIn('external_api_success', response['status'])


if __name__ == '__main__':
    unittest.main()
