from models.user_model import db, User # noqa
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token


class AuthService:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def missing(self):
        if not self.username or not self.password:
            return True

    def exists(self):
        user = User.query.filter_by(username=self.username).first()
        return bool(user)

    def create_user(self):
        new_user = User(username=self.username, password=generate_password_hash(self.password, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()

    def create_token(self, password):
        user = User.query.filter_by(username=self.username).first()
        if check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.id)
            return access_token
