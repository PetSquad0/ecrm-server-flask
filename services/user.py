from ..models import db, User
from werkzeug.security import generate_password_hash


class UserService:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def required(self):
        return bool(self.username) and bool(self.password)

    def exists(self):
        user = User.query.filter_by(username=self.username).first()
        return bool(user)

    def create(self):
        new_user = User(username=self.username, password=generate_password_hash(self.password, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()