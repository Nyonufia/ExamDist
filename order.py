from config import db
from custom import Customer

class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    createDate = db.Column(db.Date, nullable = False)
    #Clé étrangère
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable = False)
    customer = db.relationship('Customer', foreign_keys = [customer_id]) 
