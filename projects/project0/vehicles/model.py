'''Vehicle model defining vehicle class behavior and attributes'''

from project0.offers.model import Offer

class Vehicle():
    '''Class for storing vehicle information'''
    def __init__(self, db_id=-1, make='', model='', year='',
                 color='', price=0):
        self._id = db_id
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.owner = None
        self.offers = []
        self.payments = []

    def get_payments(self):
        '''Returns list of payments left'''
        return self.payments

    def get_id(self):
        '''Returns vehicle id'''
        return self._id

    def set_owner(self, owner):
        '''Returns the owner of the vehicle'''
        self.owner = owner

    def get_owner(self):
        '''Returns owner of vehicle'''
        return self.owner

    def is_available(self):
        '''Returns vehicle if not already owned'''
        return not self.owner

    def get_accepted_offer_amount(self):
        '''Returns the accepted offer on a vehicle'''
        amount = 0
        for offer in self.offers:
            if offer.get_status() == 'accepted':
                amount = offer.get_offer_amount()
        return amount

    def get_offers(self):
        '''Returns offers on a vehicle'''
        offers = []
        for off in self.offers:
            if off.get_status() == 'pending':
                offers.append(off)
        return self.offers

    def __str__(self):
        '''String representation of object Vehicle'''
        string = self.year + ' ' + self.make  + ' ' + self.model  + ' '
        string += ' for $' + '{0:.2f}'.format(self.price)
        string2 = ' '.join([str(v) for v in self.offers])
        if self.owner:
            string += ' SOLD to ' + str(self.owner)
        string += ' ' + string2
        return string

    def __repr__(self):
        '''Returns representation of object'''
        return self.__str__()

    def to_dict(self):
        '''Creates and returns a dictionary representation of vehicle instance'''
        dict_rep = self.__dict__
        if self.offers != []:
            for i in range(len(self.offers)):
                dict_rep['offers'][i] = self.offers[i].to_dict()
        return dict_rep

    @classmethod
    def from_dict(cls, input_dict: dict):
        '''Creates an instance of the class from a dictionary input'''
        vehicle = Vehicle()
        vehicle.__dict__.update(input_dict)
        if vehicle.offers != []:
            for i in range(len(vehicle.offers)):
                vehicle.offers[i] = Offer().from_dict(vehicle.offers[i])
        return vehicle
