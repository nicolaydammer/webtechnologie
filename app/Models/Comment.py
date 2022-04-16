from app import db


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(50))
    user = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, comment, user):
        self.comment = comment
        self.user = user
