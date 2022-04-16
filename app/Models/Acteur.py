from app import db


class Acteur(db.Model):
    __tablename__ = 'acteurs'

    id = db.Column(db.Integer, primary_key=True)
    voornaam = db.Column(db.String(50))
    achternaam = db.Column(db.String(50))
    film = db.relationship('Film', uselist=False)

    def __init__(self, voornaam, achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam
