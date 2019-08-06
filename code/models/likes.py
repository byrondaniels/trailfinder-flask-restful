from db import db


class LikesModel(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    like = db.Column(db.Boolean)
    date = db.Column(db.Date)

    def __init__(self, user, post, like):
        self.post = post
        self.user = user
        self.like = like
        self.data = datetime.today()

    @classmethod
    def find_by_post(cls, post):
        return cls.query.filter_by(post=post)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
