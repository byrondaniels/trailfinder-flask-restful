from db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(180), nullable=False)
    avatar = db.Column(db.String(80))
    date = db.Column(db.Date)

    def __init__(self, name, email, password, avatar):
        self.name = name
        self.email = email
        self.avatar = avatar
        self.password = generate_password_hash(password)
        self.data = datetime.today()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def check_password(self, password):
        return check_password_hash(self.password, password)
