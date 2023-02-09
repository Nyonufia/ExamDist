from config import db
from payement import Payement

class Cash(Payement):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    cashTendered = db.Column(db.Float, nullable = False)

    __mapper_args__ = {
        'polymorphic_identity':'cash',
        #'polymorphic_load': 'inline'
    }
'''
    def__init__(self, cashTendered):
        super().__init__(amount, cashTendered)
        self.cashTendered = cashTendered

    def__repr__(self):
        return f'Cash: {self.cashTendered}'
'''