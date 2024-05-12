from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login, db

class Users(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

    def set_password(self, pw):
        self.password = generate_password_hash(pw)

    def check_password(self, pw):
        print("Checking password hash - db has " + self.password + " form has: " + pw)
        return check_password_hash(self.password, pw)

    @login.user_loader
    def load_user(id):
        return db.session.get(Users, int(id))

