from app import db


class Commentaar(db.Model):
    __tablename__ = 'commentaar'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(50))
    user = db.relationship('User', backref='User', uselist=False)

    def __init__(self, comment, user):
        self.comment = comment
        self.user = user
