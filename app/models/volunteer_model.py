from app import db

class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    preferences = db.Column(db.String(200))

    def __repr__(self):
        return f"Volunteer('{self.name}', '{self.email}')"
