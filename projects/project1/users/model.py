'''Defining users behavior and attributes '''
import json

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
        self.application_info = None
        self.loans = []

    def set_application(self, application):
        '''Sets the application info of the user'''
        self.application_info = application

    def set_id(self, db_id):
        '''Sets user's id'''
        self._id = db_id

    def get_id(self):
        '''Returns the user's id'''
        return self._id

    def set_role(self, role):
        '''Sets the user's role'''
        self.role = role

    def get_role(self):
        '''Returns the user's role'''
        return self.role

    def get_loans(self):
        '''Returns the user's loans'''
        return self.loans

    def to_dict(self):
        '''Returns the dictionary representation of itself'''
        return self.__dict__

    def __str__(self):
        '''Returns string representation of object'''
        string = 'User: ' + self.username + ' ' + self.password + ' ' + self.firstname
        string += ' ' + self.lastname
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

class ApplicationInfo():
    '''A class that defines attributes and how ApplicationInfo should behave'''
    def __init__(self, username='', firstname='', lastname='', age=0, ssn='', gender='',
                 employer='', title='', salary=0, expenses=0, b_street='', b_city='',
                 b_state='', b_zip='', m_street='', m_city='', m_state='', m_zip=''):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.ssn = ssn
        self.title = title
        self.employer = employer
        self.salary = salary
        self.expenses = expenses
        self.b_street = b_street
        self.b_city = b_city
        self.b_state = b_state
        self.b_zip = b_zip
        self.m_street = m_street
        self.m_city = m_city
        self.m_state = m_state
        self.m_zip = m_zip

    def to_dict(self):
        '''Returns the dictionary representation of itself'''
        return self.__dict__

    def __str__(self):
        '''Returns string representation of an object'''
        string = 'Application: ' + self.username
        return string

    def __repr__(self):
        '''Returns representation of object'''
        return self.__str__()

    @classmethod
    def from_dict(cls, input_apply):
        '''Creates an instance of the class from a dictionary'''
        apply = ApplicationInfo()
        apply.__dict__.update(input_apply)
        return apply


class ItemEncoder(json.JSONEncoder):
    ''' Allows us to serialize our objects as JSON '''
    def default(self, o):
        return o.to_dict()
