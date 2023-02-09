from config import db
from payement import Payement

class Check(Payement):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(120), nullable = False)
    bankID = db.Column(db.String(120), nullable = False)

    __mapper_args__ = {
        'polymorphic_identity':'check',
        #'polymorphic_load': 'inline'
    }