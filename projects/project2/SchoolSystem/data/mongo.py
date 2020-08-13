'''Modularization of Mongo data access
    Define all of our CRUD (Create, Read, Update, and Delete)
    in this file  to separate those concerns'''

#pylint: disable=R0913
import os
import pymongo
from SchoolSystem.users.model import User, Student
from SchoolSystem.assignments.model import Assignment
from SchoolSystem.submissions.model import Submission
from SchoolSystem.data.msgrModel import Messager
from SchoolSystem.updates.model import Update
from SchoolSystem.schedules.model import Schedule
from SchoolSystem.data.logger import get_logger

_log = get_logger(__name__)

try:
    _scl = pymongo.MongoClient(os.environ.get('TroyMongoURI')).project2
except:
    _log.exception('Could not connect to Mongo')
    raise

def get_user_by_id(db_id: int):
    '''Returns a user by their id'''
    return User.from_dict(_scl.users.find_one({'_id': db_id}))

def get_submissions(teacher):
    '''Gets all submissions'''
    dict_list = _scl.submissions.find({'teacher': teacher})
    return [Submission.from_dict(submission) for submission in dict_list]

def get_requirements(requirements):
    '''Gets all requirements'''
    _log.info('Attempting to retrieve all users from database')
    dict_list = _scl.users.find({'username': requirements})
    return [User.from_dict(user) for user in dict_list]


def get_users():
    '''Read all the users from the collection'''
    _log.info('Attempting to retrieve all users from database')
    dict_list = _scl.users.find()
    return [User.from_dict(user) for user in dict_list]

def login(username):
    '''A function that takenano s in a username and returns a user object'''
    _log.info('Attempting to retrieve user from database')
    _log.debug(username)
    _log.debug(type(username))
    query_dict = {'username': username}
    user_dict = _scl.users.find_one(query_dict)
    _log.debug(user_dict)
    return User.from_dict(user_dict) if user_dict else None

def remove_user(fullname: str):
    '''Removes a user from the database'''
    _log.info('Attempting to remove user from database')
    _log.debug(fullname)
    query = {"fullname": fullname}
    _scl.users.delete_one(query)

def _get_id():
    '''Retrieves the next id in the database and increments it'''
    return _scl.counter.find_one_and_update({'_id': 'UNIQUE_COUNT'},
                                            {'$inc': {'count': 1}},
                                            return_document=pymongo.ReturnDocument.AFTER)['count']

def get_assignments():
    '''Gets all assignments'''
    dict_list = _scl.assignments.find()
    return [Assignment.from_dict(assignment) for assignment in dict_list]

def insert_assignment(assignment):
    '''Creates a new assignment'''
    assignment['_id']=_get_id()
    _scl.assignments.insert_one(assignment)
    return assignment

def get_students():
    '''Gets all students'''
    dict_list = _scl.users.find({'role': 'student'})
    return [User.from_dict(user) for user in dict_list]

def get_teachers():
    '''Gets all teachers'''
    dict_list = _scl.users.find({'role': 'teacher'})
    return [User.from_dict(user) for user in dict_list]

def get_updates():
    '''Gets all updates'''
    dict_list = _scl.updates.find()
    return [Update.from_dict(update) for update in dict_list]


def update_student(username):
    '''Updates a specific student'''
    my_query = {'username': str(username)}
    new_data = _scl.updates.find_one(my_query)
    _log.info(new_data)
    _log.info(new_data['update_info']['username'])
    result = _scl.users.update_one(my_query,
                                   {'$set': {'username': new_data['update_info']['username'],
                                   'password': new_data['update_info']['password'],
                                   'address': new_data['update_info']['address']}})
    new_query = {'username': str(new_data['update_info']['username'])}
    newUser = _scl.users.find_one(new_query)
    _scl.updates.delete_one(my_query)
    return Student.from_dict(newUser)

def delete_update(username):
    '''Deletes a user'''
    _log.debug(username)
    my_query = {'username': str(username)}
    _scl.updates.delete_one(my_query)

def get_schedules():
    '''Gets all schedules'''
    dict_list = _scl.schedules.find()
    return [Schedule.from_dict(schedule) for schedule in dict_list]

def update_schedule(username):
    '''Updates a schedule'''
    my_query = {'username': str(username)}
    schedule_request = _scl.schedules.find_one(my_query)
    _log.info(schedule_request)
    result = _scl.users.update_one(my_query, {'$set': {'current_schedule.period_1': schedule_request['schedule']['period_1'],
                                                      'current_schedule.period_2': schedule_request['schedule']['period_2'],
                                                      'current_schedule.period_3': schedule_request['schedule']['period_3'],
                                                      'current_schedule.period_4': schedule_request['schedule']['period_4'],
                                                      'current_schedule.period_5': schedule_request['schedule']['period_5']}})
    student = _scl.users.find_one(my_query)
    _scl.schedules.delete_one(my_query)
    return Student.from_dict(student)

def delete_schedule_update(username):
    '''Deletes a schedule update'''
    _log.info(username)
    my_query = {'username': username}
    _scl.schedules.delete_one(my_query)

def sumbit_schedule_update(username, new_schedule):
    '''Creates a schedule update'''
    my_query = {'username': username}
    input_dict = Schedule(_get_id(), username, new_schedule).to_dict()
    _scl.schedules.insert_one(input_dict)
    result = _scl.schedules.find_one(my_query)
    _log.debug(result)

def submit_student_update(username, new_data):
    '''Creates a new update'''
    my_query = {'username': username}
    input_dict = Update(_get_id(), username, new_data).to_dict()
    _scl.updates.insert_one(input_dict)
    result = _scl.updates.find_one(my_query)
    _log.debug(result)

def update_user(username, new_profile):
    '''Updates a user'''
    myquery = {"username": username}
    _log.info(new_profile)
    _scl.users.update_one(myquery, {'$set': new_profile})

def assign_teacher(username, new_data):
    '''Assigns a teacher to a student'''
    myquery = {"username": username}
    _log.info(new_data)
    _scl.users.update_one(myquery, {'$set': new_data})

def edit_admin(name, new_data):
    '''Edits an admin's information'''
    myquery = {"username": name}
    _scl.users.update_one(myquery, {'$set': new_data})

def grade_homework(homework, new_data):
    '''Allows teacher to grade homework'''
    my_query = {"_id": homework}
    _scl.submissions.update_one(my_query, {'$set': new_data})

def add_submission(submission):
    '''Creates a new submission'''
    submission['_id']=_get_id()
    _scl.submissions.insert_one(submission)
    return submission

def add_user(user):
    '''Adds a new user'''
    _log.debug('querying db')
    _log.debug(user)
    query_dict = {'username': user['username']}
    user_dict = _scl.users.find_one(query_dict)
    if user_dict is None:
        _log.debug('no user of that username, adding user')
        user['_id'] = _get_id()
        _log.debug(user['_id'])
        try:
            _log.debug(user['_id'])
            _scl.users.insert_one(user)
            return user
        except:
            pass

def get_msgs(msg_to):
    '''Gets all messages'''
    _log.debug(msg_to)
    query_dict = {"msg_to": msg_to}
    dict_list = _scl.messager.find(query_dict)
    msg_list = []
    for msg in dict_list:
        msg_list.append(Messager().from_dict(msg))
    _log.debug(str(msg_list))
    return msg_list

def new_msg(message):
    '''Creates a new message'''
    message['_id'] = str(_get_id())
    try:
        _scl.messager.insert_one(message)
        return message
    except:
        pass

if __name__ == '__main__':
    _log.info('Running Mongo script: dropping collections from project2 database')
    _log.info(_scl.list_collection_names())
    _scl.counter.drop()

    _scl.counter.insert_one({'_id': 'UNIQUE_COUNT', 'count': 0})
