from config import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(150), nullable = False)
    deliveryAddress = db.Column(db.String(150), nullable = True)
    contact = db.Column(db.Integer, nullable = True)
    active = db.Column(db.Boolean, nullable = False)