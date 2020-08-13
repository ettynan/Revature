'''Offer module defining offer class behavior and attributes'''

class Offer():
    '''Class for storing offer information'''
    def __init__(self, db_id=-1, offer_amount=0.0, customer_id=None, vehicle_id=None):
        self._id = db_id
        self.status = 'pending'
        self.offer_amount = offer_amount
        self.customer_id = customer_id

    def get_offer_amount(self):
        return self.offer_amount

    def get_status(self):
        '''Returns the status of an offer'''
        return self.status

    def set_status(self, offer):
        '''Sets the status of an offer'''
        self.status = offer

    def get_customer_id(self):
        '''Returns the customer user id'''
        return self.customer_id

    def __str__(self):
        '''Returns string representation'''
        string = str(self.customer_id) + ': '
        string += 'offer of: $' + self.offer_amount + ' is ' + self.status
        return string

    def __repr__(self):
        '''Returns representation of object'''
        return self.__str__()

    def to_dict(self):
        '''Creates and returns a dictionary representation of offer instance'''
        return self.__dict__

    @classmethod
    def from_dict(cls, input_offer):
        '''Creates an instance of the class from a dictionary'''
        offer = Offer()
        offer.__dict__.update(input_offer)
        return offer
