from flask import Blueprint, jsonify, request
from services.auth_service import AuthService # noqa

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/api/v0.1/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    auth_service = AuthService(username, password)

    if auth_service.missing():
        return jsonify({"message": "Username and password are missing"}), 400

    if auth_service.exists():
        return jsonify({"message": "User already exists"}), 400

    auth_service.create_user()

    return jsonify({"message": "The user has been successfully created"}), 201


@auth_blueprint.route('/api/v0.1/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    auth_service = AuthService(username, password)

    if auth_service.exists():
        access_dict = {
            "access_token": auth_service.create_token(password)
        }
        return jsonify(access_dict), 200

    return jsonify({"message": "Invalid username or password"}), 401
