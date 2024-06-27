from flask import Flask, request, jsonify
import subprocess
import json
import os


app = Flask(__name__)


@app.route('/api', methods=['POST'])
def api_entry():
    json_request = request.get_json()
    if not json_request:
        return jsonify({"error": "Invalid JSON"}), 400

    # Get the absolute path of the cli_entry.py script
    cli_entry_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cli_entry.py')

    # Call the CLI entry point with the JSON request
    try:
        result = subprocess.run(
            ['python', cli_entry_path],
            input=json.dumps(json_request),
            text=True,
            capture_output=True,
            check=True
        )
        response = json.loads(result.stdout)
        return jsonify(response)
    except subprocess.CalledProcessError as e:
        return jsonify({"error": "CLI call failed", "details": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
