from app import db


class Regisseur(db.Model):
    __tablename__ = 'regisseurs'

    id = db.Column(db.Integer, primary_key=True)
    voornaam = db.Column(db.String(50))
    achternaam = db.Column(db.String(50))

    def __init__(self, voornaam, achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam
