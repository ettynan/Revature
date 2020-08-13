'''Defining users behavior and attributes '''

class User():
    '''A class that defines how Users should behave'''
    def __init__(self, db_id=-1, username='', password='',
                 firstname='', lastname='', role=''):
        self._id = db_id
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.role = role
        self.owned_vehicles = []
        self.payments = []

    def get_payments(self):
        '''Returns list of payments left'''
        return self.payments

    def get_id(self):
        '''Return user's id'''
        return self._id

    def get_role(self):
        '''Returns the user's role'''
        return self.role

    def get_owned_vehicles(self):
        '''Returns vehicles owned by user'''
        return self.owned_vehicles

    def add_vehicle_owned(self, item_id):
        '''Adds a vehicle to the user's owner list'''
        self.owned_vehicles.append(item_id)

    def to_dict(self):
        '''Returns the dictionary representation of itself'''
        return self.__dict__

    def __str__(self):
        string = 'User: ' + self.username
        return string

    def __repr__(self):
        '''Returns representation of object'''
        return self.__str__()

    @classmethod
    def from_dict(cls, input_user):
        '''Creates an instance of the class from a dictionary'''
        user = User()
        user.__dict__.update(input_user)
        return user