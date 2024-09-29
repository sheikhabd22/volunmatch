from app import db

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    contact_info = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"Organization('{self.name}', '{self.description}')"