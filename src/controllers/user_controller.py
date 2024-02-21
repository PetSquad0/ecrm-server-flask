from flask_jwt_extended import (
    JWTManager, jwt_required, get_jwt_identity
)
from flask import Blueprint, jsonify
from services.user_service import UserService  # noqa

blueprint = Blueprint('api', __name__)
jwt = JWTManager()


@blueprint.route('/api/v0.1/user/info', methods=['POST'])
@jwt_required()
def api_user_info():
    user_service = UserService(get_jwt_identity())
    info = user_service.user_info()
    if info:
        return jsonify(info), 200

    return jsonify("User not found"), 401
