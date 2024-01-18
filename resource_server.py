from flask import Flask, request
import requests

app = Flask(__name__)
AUTH_SERVER = 'http://localhost:5001/exchange'


@app.route('/resource', methods=['GET'])
def resource():
    phantom_token = request.headers.get('Authorization')
    response = requests.post(
        AUTH_SERVER, json={'phantom_token': phantom_token})
    if response.status_code == 200:
        # process the request after validation
        return 'Resource accessed', 200
    return 'Access denied', 401


if __name__ == '__main__':
    app.run(port=5002)
