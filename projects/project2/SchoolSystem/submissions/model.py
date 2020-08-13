'''Defines the model for submissions'''
#pylint: disable=R0913
import json
from SchoolSystem.data.logger import get_logger

_log = get_logger(__name__)
_SECRET_KEY = '101010101unique'

class Submission:
    '''A class that defines how Submissions should behave'''
    def __init__(self, db_id=-1, student='', assignment='', teacher='',
                 grade='', content=''):
        self._id = db_id
        self.student = student
        self.assignment = assignment
        self.teacher = teacher
        self.grade = grade
        self.content = content

    def get_id(self):
        '''Returns the id of the submission'''
        return self._id

    def set_id(self, _id):
        '''Sets the id of the submission'''
        self._id = _id

    def __str__(self):
        '''String representation of the submission'''
        string = "_id: " + str(self._id) + " student: " + self.student
        string += " Instance of: " + type(self).__name__
        return string

    def __repr__(self):
        '''Returns string representation of self'''
        return self.__str__()

    def to_dict(self):
        '''Returns the dictionary representation of itself'''
        return self.__dict__

    @classmethod
    def from_dict(cls, input_submission):
        '''Creates an instance of the class from a dictionary'''
        submission = Submission()
        submission.__dict__.update(input_submission)
        return submission


class SubmissionEncoder(json.JSONEncoder):
    ''' Allows us to serialize our objects as JSON '''
    def default(self, o):
        return o.to_dict()
