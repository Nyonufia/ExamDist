from config import db
#from payement import Payement

class Cash(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    cashTendered = db.Column(db.Float, nullable = False)
'''
    __mapper_args__ = {'polymorphic_identity':'Cash'}
'''