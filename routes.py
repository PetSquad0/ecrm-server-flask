from flask import Blueprint, jsonify

blueprint = Blueprint('api', __name__)


@blueprint.route("/api/v0.1/test", methods=["POST"])
def hello_frontend():
    return jsonify({"message": "Привет фронтенд:)"}), 200
