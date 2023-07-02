from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class User (db.Document):
    username = db.StringField(primary_key = True)
    email = db.StringField()
    password_hash = db.StringField()
    role = db.StringField(default = "USER")

    def is_active (self):
        return True

    def get_id (self):
        return self.username

    def is_authenticated (self):
        return self.authenticated

    def is_anonymous (self):
        return False

    def get_role (self):
        return self.role

    def set_password (self, password):
        self.password_hash = generate_password_hash(password)

    def check_password (self, password):
        return check_password_hash(self.password_hash, password)