from app import db


class Acteur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voornaam = db.Column(db.String(50))
    achternaam = db.Column(db.String(50))

    def __init__(self, voornaam, achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam
