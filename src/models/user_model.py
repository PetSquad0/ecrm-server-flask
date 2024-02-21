from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# БАЗОВЫЙ КЛАСС USER
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
