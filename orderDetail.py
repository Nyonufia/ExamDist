from config import db
from order import Order
from item import Item

class OrderDetail(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    qty = db.Column(db.Integer, nullable = False)
    taxStatus = db.Column(db.String(150), nullable = True)
    # Importation des clés érangères
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable = True) 
    order = db.relationship('Order', foreign_keys = [order_id])

    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable = True) 
    item = db.relationship('Item', foreign_keys = [item_id])