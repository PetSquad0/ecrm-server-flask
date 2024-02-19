from flask import Flask
from config import secret_key
from routes import blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(debug=True)