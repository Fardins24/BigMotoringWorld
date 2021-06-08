from application import db

class Cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_manufacturer = db.Column(db.String(50), nullable=False)
    car_colour = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(600), nullable=False)