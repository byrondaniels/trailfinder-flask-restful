from db import db


class ProfileModel(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # The below is a list of ItemModels
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name
