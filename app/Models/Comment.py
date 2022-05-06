from app import db


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(50))
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    film = db.Column(db.Integer, db.ForeignKey('films.id'))

    def __init__(self, comment, user, film):
        self.comment = comment
        self.user = user
        self.film = film
