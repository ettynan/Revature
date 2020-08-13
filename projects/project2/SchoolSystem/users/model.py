'''Defines the model for users'''
#pylint: disable=R0913
import json
import datetime
import jwt
from SchoolSystem.data.logger import get_logger

_log = get_logger(__name__)
_SECRET_KEY = '101010101unique'

class User:
    '''A class that defines how Users should behave'''
    def __init__(self, db_id=-1, fullname='', username='', password='',
                 address='', role=''):
        self._id = db_id
        self.fullname = fullname
        self.username = username
        self.password = password
        self.address = address
        self.role = role

    def get_id(self):
        '''Returns the id of the user'''
        return self._id

    def set_id(self, _id):
        '''Sets the id of the user'''
        self._id = _id

    def login(self, username, password):
        '''Returns true id username and password match existing'''
        return self.username == username and self.password == password

    def __str__(self):
        '''String representation of the user'''
        string = "_id: " + str(self._id) + " fullname: " + self.fullname
        string += " Instance of: " + type(self).__name__
        return string

    def __repr__(self):
        '''Returns string representation of self'''
        return self.__str__()

    def to_dict(self):
        '''Returns the dictionary representation of itself'''
        return self.__dict__

    def get_role(self):
        '''returns the role of the user'''
        return self.role

    @classmethod
    def from_dict(cls, input_user):
        '''Creates an instance of the class from a dictionary'''
        user = User()
        user.__dict__.update(input_user)
        return user

    def encode_auth_token(self):
        ''' Generate an authentication token for this user '''
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': self._id
            }
            _log.debug("payload set")
            return jwt.encode(payload, _SECRET_KEY, algorithm='HS256')
        except Exception as e:
            _log.exception('Encode failed.')
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        ''' Decode the auth token to receive the id of user '''
        try:
            payload = jwt.decode(auth_token, _SECRET_KEY)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Token expired. please login again.'
        except jwt.InvalidTokenError:
            return 'Token invalid. Please login.'

class Admin(User):
    '''A class that defines how Admins should behave'''
    def __init__(self, db_id=-1, fullname='', username='', password='',
                 address='', role=''):
        super(). __init__(db_id, fullname, username, password, address, role)

class Teacher(User):
    '''A class that defines how Teachers should behave'''
    def __init__(self, db_id=-1, fullname='', username='', password='', role='',
                 substitute=False, ):
        super(). __init__(db_id, fullname, username, password, role)
        self.assigned_students = []
        self.courses = []
        self.substitute = substitute


class Student(User):
    '''A class that defines how Students should behave'''
    def __init__(self, db_id=-1, fullname='', username='', password='',
                 address='', current_schedule={}, teacher='', role='', grades=[],
                 grade_level='', age=0, english=0, math=0, science=0, social_studies=0):
        super(). __init__(db_id, fullname, username, password, address, role)
        self.grades = grades
        self.current_schedule = current_schedule
        self.grade_level = grade_level
        self.age = age
        self.teacher = teacher
        self.english = english
        self.math = math
        self.science = science
        self.social_studies = social_studies


class UserEncoder(json.JSONEncoder):
    ''' Allows us to serialize our objects as JSON '''
    def default(self, o):
        return o.to_dict()
