from flask_bcrypt import check_password_hash
from flask_login import UserMixin
from app import db, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash


@LoginManager.user_loader
def load_user(user_id):
    return User.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)
