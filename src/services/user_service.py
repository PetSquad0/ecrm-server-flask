from models.user_model import User # noqa


class UserService:
    def __init__(self, id):
        self.id = id

    def user_info(self):
        user = User.query.filter_by(id=self.id).first()
        if user:
            user_info_dict = {"id": user.id,
                              "username": user.username,
                              "role": user.role,
                              "created_at": user.created_at}

            return user_info_dict
