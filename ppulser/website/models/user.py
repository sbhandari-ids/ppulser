from website.database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(350))
    username = db.Column(db.String(150))
    age = db.Column(db.String(150))
    phone = db.Column(db.String(150))
