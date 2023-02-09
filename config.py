from app import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app.config['SECRET_KEY'] ="root"

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/order-dba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db=SQLAlchemy(app)