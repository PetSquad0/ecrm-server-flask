from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

blueprint = Blueprint('api', __name__)
jwt = JWTManager()


@blueprint.route('/api/v0.1/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"message": "Имя пользователя и пароль обязательны"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Пользователь уже существует"}), 400

    new_user = User(username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Пользователь успешно создан"}), 201


@blueprint.route('/api/v0.1/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)

        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Неверное имя пользователя или пароль"}), 401


@blueprint.route('/api/v0.1/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    return jsonify({"logged_in_as": user.username,
                    "role": user.role}), 200


def init_jwt(app):
    jwt.init_app(app)


@jwt.invalid_token_loader
def invalid_token_callback():
    return jsonify({"message": "Неверный токен"}), 401


@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({"message": "Срок действия токена истек"}), 401


@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({"message": "Токен отозван"}), 401


@jwt.needs_fresh_token_loader
def needs_fresh_token_callback():
    return jsonify({"message": "Требуется свежий токен"}), 401
