from app import db


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(50))
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    film = db.relationship('Film', uselist=False)

    def __init__(self, comment, user):
        self.comment = comment
        self.user = user
