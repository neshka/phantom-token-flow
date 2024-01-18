from flask import Flask, request, jsonify
import jwt
import uuid

app = Flask(__name__)
SECRET_KEY = 'your_secret_key'


@app.route('/token', methods=['POST'])
def token():
    # issues JWT
    real_token = jwt.encode({'user': 'example_user'},
                            SECRET_KEY, algorithm='HS256')
    return jsonify(real_token=real_token)


@app.route('/exchange', methods=['POST'])
def exchange():
    # exchange phantom token for JWT
    phantom_token = request.json.get('phantom_token')
    if phantom_token == 'valid_phantom_token':
        real_token = jwt.encode(
            {'user': 'example_user'}, SECRET_KEY, algorithm='HS256')
        return jsonify(real_token=real_token)
    return 'Invalid phantom token', 401


if __name__ == '__main__':
    app.run(port=5001)
