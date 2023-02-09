from config import db
from payement import Payement

class Credit(Payement):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    number = db.Column(db.String(120), nullable = False)
    typ = db.Column(db.String(120), nullable = False)
    expireDate = db.Column(db.Date, nullable = False)

    __mapper_args__ = {
        'polymorphic_identity':'credit',
        #'polymorphic_load': 'inline'
    }