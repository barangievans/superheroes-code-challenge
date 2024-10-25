from app import db

class Hero(db.Model):
    __tablename__ = 'heroes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    
    powers = db.relationship('HeroPower', backref='hero', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "powers": [hp.power_id for hp in self.powers]
        }

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "description": self.description,
        }

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(50), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)
