from config import db
from order import Order

class Payement(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    amount = db.Column(db.Float, nullable = False)
    #Clé étrangère
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable = True) 
    order = db.relationship('Order', foreign_keys = [order_id])
'''
    payementMode = ""
    __mapper_args__ = {'polymorphic_on':payementMode}
'''