from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash
from models import User
from services.user import UserService

blueprint = Blueprint('api', __name__)
jwt = JWTManager()


@blueprint.route('/api/v0.1/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    user_service = UserService(username, password)

    if user_service.required():
        return jsonify({"message": "Username and password are required"}), 400

    if user_service.exists():
        return jsonify({"message": "User already exists"}), 400

    user_service.create()

    return jsonify({"message": "The user has been successfully created"}), 201


@blueprint.route('/api/v0.1/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username, password=password).first()

    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200

    return jsonify({"message": "Invalid username or password"}), 401


@blueprint.route('/api/v0.1/user/info', methods=['POST'])
@jwt_required()
def user_info():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    return jsonify({"id": user.id,
                    "username": user.username,
                    "role": user.role,
                    "created_at": user.created_at}), 200
