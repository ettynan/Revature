'''Defines the model for users'''
import json
from SchoolSystem.data.logger import get_logger

_log = get_logger(__name__)
_SECRET_KEY = '101010101unique'

class Assignment:
    '''A class that defines how Assignments should behave'''
    def __init__(self, db_id=-1, name='', description=''):
        self._id = db_id
        self.name = name
        self.description = description


    def get_id(self):
        '''Returns the id of the assignment'''
        return self._id

    def set_id(self, _id):
        '''Sets the id of the assignment'''
        self._id = _id

    def __str__(self):
        '''String representation of the assignment'''
        string = "_id: " + str(self._id) + " name: " + self.name
        string += " Instance of: " + type(self).__name__
        return string

    def __repr__(self):
        '''Returns string representation of self'''
        return self.__str__()

    def to_dict(self):
        '''Returns the dictionary representation of itself'''
        return self.__dict__

    @classmethod
    def from_dict(cls, input_assignment):
        '''Creates an instance of the class from a dictionary'''
        assignment = Assignment()
        assignment.__dict__.update(input_assignment)
        return assignment


class AssignmentEncoder(json.JSONEncoder):
    ''' Allows us to serialize our objects as JSON '''
    def default(self, o):
        return o.to_dict()
