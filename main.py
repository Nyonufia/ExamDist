import pymysql
from app import app
from flask_cors import CORS
from config import db
from custom import Customer
from item import Item
from order import Order
from orderDetail import OrderDetail
from payement import Payement
from cash import Cash
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
        if createDate and deliveryAddress and contact and active and  request.method=='POST':
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

if(__name__=='__main__'):
    app.run()