from db import db


class SocialMediaModel(db.Model):
    __tablename__ = 'social_medias'

    id = db.Column(db.Integer, primary_key=True)
    profile = db.Column(db.Integer, db.ForeignKey(
        'profiles.id'), nullable=False)
    youtube = db.Column(db.String(60))
    twitter = db.Column(db.String(60))
    facebook = db.Column(db.String(60))
    linkedin = db.Column(db.String(60))
    instagram = db.Column(db.String(60))

    def __init__(self, profile, youtube, twitter, facebook, linkedin, instagram):
        self.profile = profile
        self.youtube = youtube
        self.twitter = twitter
        self.facebook = facebook
        self.linkedin = linkedin
        self.instagram = instagram

    def find_by_profile(cls, profile):
        return cls.query.filter_by(profile=profile).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
