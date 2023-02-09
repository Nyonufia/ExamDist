from config import db
#from payement import Payement

class WireTransfert(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)    
    bankID = db.Column(db.String(120), nullable = False)
    bankName = db.Column(db.String(120), nullable = False)

    __mapper_args__ = {
        'polymorphic_identity':'wireTransfert',
        #'polymorphic_load': 'inline'
    }