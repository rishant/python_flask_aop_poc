import sys
import json
from service_registry import handle_request


def main():
    try:
        # Read JSON input from stdin
        input_data = sys.stdin.read()
        json_request = json.loads(input_data)

        # Call the handle_request function
        response = handle_request(json_request)

        # Print the response as JSON
        print(json.dumps(response))
    except Exception as e:
        # Handle any exceptions
        print(json.dumps({"error": str(e)}))


if __name__ == '__main__':
    main()
