import pymysql
from app import app
from flask_cors import CORS
from config import db
from custom import Customer
from item import Item
from order import Order
from orderDetail import OrderDetail
from orderStatus import OrderStatus
from payement import Payement
from cash import Cash
from check import Check
from credit import Credit
from wireTransfert import WireTransfert
from orderStatus import OrderStatus
from flask import jsonify, Flask, request

app.app_context().push()
db.drop_all()
db.create_all()

@app.route('/customer/add', methods=['POST'])
def addCustomer():
    try:
        json = request.json
        name = json['name']
        deliveryAddress = json['deliveryAddress']
        contact = json['contact']
        active = json['active']
        if name and deliveryAddress and contact and active and  request.method=='POST':
            customer = Customer(name=name, deliveryAddress=deliveryAddress, contact=contact, active=active)            
            db.session.add(customer)
            db.session.commit()
            reponse = jsonify('Client ajouté')
            #reponse.status_code = 200
            return reponse
    except Exception as e:
        print(e)
        reponse = {"status_code": 404, "message":"erreur"}
        return jsonify(reponse)
    finally:
        db.session.rollback()
        db.session.close()

@app.route('/order/add', methods=['POST'])
def addOrder():
    try:
        json = request.json
        createDate = json['createDate']
        customer_id = json['customer_id']
        if createDate and request.method=='POST':
            order = Order(createDate=createDate)
            if customer_id:
                customer = Customer.query.filter_by(id=customer_id).first()
                print(customer)
                order.customer = customer
            db.session.add(order)
            db.session.commit()
            reponse = jsonify('Employé ajouté')
            #reponse.status_code = 200
            return reponse
    except Exception as e:
        print(e)
        reponse = {"status_code": 404, "message":"erreur"}
        return jsonify(reponse)
    finally:
        db.session.rollback()
        db.session.close()


@app.route('/orderStatus/add', methods=['POST'])
def addOrderStatus():
    try:
        json = request.json
        CREATE = json['CREATE']
        SHIPPING = json['SHIPPING']
        DELIVERED = json['DELIVERED']
        PAID = json['PAID']
        if CREATE and SHIPPING and DELIVERED and PAID and request.method =='POST':
            orderStatus = OrderStatus(CREATE = CREATE, SHIPPING =SHIPPING, DELIVERED=DELIVERED, PAID=PAID)
            db.session.add(orderStatus)
            db.session.commit()
            reponse = jsonify('Statut de commande ajouté')
            #reponse.status_code = 200
            return reponse
    except Exception as e:
        print(e)
        reponse = {"status_code": 404, "message":"erreur"}
        return jsonify(reponse)
    finally:
        db.session.rollback()
        db.session.close()

@app.route('/payement/add', methods=['POST'])
def addPayement():
    try:
        json = request.json
        amount = json["amount"]
        if amount and request.method =='POST':
            payement = Payement(amount= amount)
            if order_id:
                order = Order.query.filter_by(id=order_id).first()
                print(order)
                payement.order = order
            db.session.add(payement)
            db.session.commit()
            reponse = jsonify('Payement ajouté')
            #reponse.status_code = 200
            return reponse
    except Exception as e:
        print(e)
        reponse = {"status_code": 404, "message":"erreur"}
        return jsonify(reponse)
    finally:
        db.session.rollback()
        db.session.close()

if(__name__=='__main__'):
    app.run()