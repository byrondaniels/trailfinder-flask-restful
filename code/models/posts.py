from db import db


class PostsModel(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    text = db.Column(db.String(280), nullable=False)
    name = db.Column(db.String(80))
    avatar = db.Column(db.String(280))
    likes = db.relationship('LikesModel', lazy='dynamic')
    comments = db.relationship('CommentsModel', lazy='dynamic')
    date = db.Column(db.Date)

    def __init__(self, user, text, name, avatar):
        self.name = name
        self.user = user
        self.text = text
        self.name = name
        self.avatar = avatar

    @classmethod
    def find_by_user(cls, user):
        return cls.query.filter_by(user=user).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
