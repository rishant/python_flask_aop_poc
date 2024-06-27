# curl -X POST http://127.0.0.1:5000/api
# -H "Content-Type: application/json"
# -d '{"method": "user_create", "params": {"param": "test_user"}}'

import unittest
from app import app
import os


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Change the working directory to the root of the project
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

    def test_api_entry_user(self):
        response = self.app.post('/api', json={
            "method": "user_create",
            "params": {"param": "test_user"}
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_create_success', response.get_json()['status'])

    def test_api_entry_invalid_json(self):
        response = self.app.post('/api', data="Invalid JSON")
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
