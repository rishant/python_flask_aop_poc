import unittest
import subprocess
import json
import os


class TestCliEntry(unittest.TestCase):

    def test_cli_entry_user_create(self):
        # Get the absolute path of the cli_entry.py script
        # cli_entry_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cli_entry.py')

        cli_entry_path = "E:\\Code Practices\\python\\python_flask_aop_poc\\cli_entry.py"

        result = subprocess.run(
            ['python', cli_entry_path],
            input=json.dumps({"method": "user_create", "params": {"param": "test_user_create"}}),
            text=True,
            capture_output=True,
            check=True
        )
        response = json.loads(result.stdout)
        self.assertIn('user_create_success', response['status'])


if __name__ == '__main__':
    unittest.main()
