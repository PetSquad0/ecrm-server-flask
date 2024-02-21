from flask import Flask
from config import secret_key, jwt_secret_key
from controllers.user_controller import blueprint, jwt
from controllers.auth_controller import auth_blueprint
from models.user_model import db

app = Flask(__name__)

app.register_blueprint(blueprint)
app.register_blueprint(auth_blueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = secret_key
app.config['JWT_SECRET_KEY'] = jwt_secret_key

db.init_app(app)
jwt.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
