from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class UserProfile(db.Model, UserMixin):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(128), nullable=False) #password

    def __init__(self, first_name, last_name, username, password):
        self.fist_name = first_name
        self.last_name = last_name
        self.username = username 
        self.new_password(password)

    def new_password(self, password):
        self.password = generate_password_hash(password)

    def password_check(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)  # python 3 support

    def __repr__(self):
        return f'<User {self.username}>'