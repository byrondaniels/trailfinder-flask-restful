from db import db
from datetime import datetime


class CommentsModel(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    text = db.Column(db.String(180), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    avatar = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date)

    def __init__(self, post, user, text, name, avatar):
        self.post = post
        self.user = user
        self.text = text
        self.name = name
        self.avatar = avatar
        self.date = datetime.today()

    @classmethod
    def find_by_post(cls, post):
        return cls.query.filter_by(post=post)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
