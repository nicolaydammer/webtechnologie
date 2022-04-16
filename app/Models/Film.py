from app import db


class Film(db.Model):
    __tablename__ = 'films'

    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String(50))
    regisseur = db.Column(db.Integer, db.ForeignKey('regisseurs.id'))
    acteur = db.Column(db.Integer, db.ForeignKey('acteurs.id'))

    def __init__(self, titel, regisseur, acteur):
        self.titel = titel
        self.regisseur = regisseur
        self.acteur = acteur
