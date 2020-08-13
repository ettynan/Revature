'''Modularization of Mongo data access
    Define all of our CRUD (Create, Read, Update, and Delete)
    in this file  to separate those concerns'''

import os
import sys
import getpass
import pymongo

from project1.users.model import User, ApplicationInfo
from project1.loans.model import Loan
from project1.data.logger import get_logger

_log = get_logger(__name__)

try:
    _bank = pymongo.MongoClient(os.environ.get('MONGO_URI')).project1
except:
    _log.exception('Could not connect to Mongo')
    raise

def get_user_by_id(db_id):
    '''Returns the user_by user id'''
    _log.info('Attempting to retrieve user from database')
    query = {'_id': db_id}
    user = _bank.users.find_one(query)
    return User.from_dict(user) if user else None

def get_user_by_username(username):
    '''Returns the user_by username'''
    _log.info('Attempting to retrieve user from database')
    query_dict = {'username': username}
    user = _bank.users.find_one(query_dict)
    return User.from_dict(user) if user else None

# def get_users():
#     '''Read all the users from the collection'''
#     dict_list = _bank.users.find({},{'_id':0}) #projection might need to be removed
#     return [User.from_dict(user) for user in dict_list]

def get_user(username):
    query = {'username': username}
    try:
        user = _bank.users.find_one(query)
        return User.from_dict(user)
    except Exception:
        _log.exception('Unable to retrieve user info')
        return None

def get_users():
    '''Returns all users in the system'''
    try:
        dict_list = _bank.users.find()
        return [User.from_dict(user) for user in dict_list]
    except Exception:
        _log.exception('Unable to retrieve all users')
        return None

def get_loans_needing_approval():
    '''Returns all the loans in the system needing approval'''
    loans_list = []
    users = get_users()
    try:
        for user in users:
            for loan in user.loans:
                if loan['status'] == 'Loan Manager Approval Needed':
                    loans_list.append(loan) # not a loan object yet, just the info
        _log.debug(loans_list)
        return loans_list
    except Exception:
        _log.exception('Unable to retrieve all loans needing approval')
        return None

def login(username, password):
    '''A function that takes in a username and password and returns user object'''
    _log.info('\nAttempting to retrieve user from database')
    query_dict = {'username': username, 'password': password}
    try:
        user_dict = _bank.users.find_one(query_dict)
        return User.from_dict(user_dict) if user_dict else None
    except BaseException:
        _log.exception('user not found')
        return None

def add_loan_application_to_user(username, application, loan: Loan):
    '''Update a user with an application for a loan'''
    query = {'username': username}
    try:
        _bank.users.update_one(query, {'$set': {'application_info': application.to_dict()}})
        _bank.users.update_one(query, {'$push': {'loans': loan.to_dict()}})
    except Exception:
        _log.exception('unable to create application for user')

def create_loan(username, loan):
    '''Creates a new user in the database'''
    _log.debug('in crate loan db %s', loan)
    loan._id = _get_id()
    query = {'username', username}
    try:
        _bank.users.update_one(query, {'$push': {'loans': loan.to_dict()}})
        _log.info('Yay, new loan made!')
    except Exception:
        _log.exception('unable to create loan')

def create_user(user):
    '''Creates a new user in the database'''
    user.set_id(_get_id())
    try:
        _bank.users.insert_one(user.to_dict())
        _log.info('Yay, new user made!')
    except Exception:
        _log.exception('unable to create user')

def get_user_info_by_username(username):
    '''Displays user information including loans'''
    query = {'username': username}
    user = _bank.users.find_one(query)
    return User.from_dict(user) if user else None

def approve_loan(loan):
    '''Takes in a status of approved and updates the loan's status'''
    try:
        query = {'loans.loan_type': loan['loan_type'],
                 'loans.risk_score': loan['risk_score'],
                 'loans.credit_score': loan['credit_score']}
        _bank.users.update_many(query, {'$set': {'loans.$.status': 'Approved'}})
    except Exception:
        _log.info('Unable to approve loan')

def deny_loan(loan):
    '''Takes in a status of denied and updates the loan's status'''
    try:
        query = {'loans.loan_type': loan['loan_type'],
                 'loans.risk_score': loan['risk_score'],
                 'loans.credit_score': loan['credit_score']}
        _bank.users.update_many(query, {'$set': {'loans.$.status': 'Denied'}})
        _log.info('Loan denied')
    except Exception:
        _log.info('Unable to deny loan')

def _get_id():
    '''Retrieves the next id in the database and increments it'''
    return _bank.counter.find_one_and_update({'_id': 'UNIQUE_COUNT'},
                                            {'$inc': {'count': 1}},
                                            return_document=pymongo.ReturnDocument.AFTER)['count']

if __name__ == '__main__':
    _log.info('Running Mongo script: dropping collections from project1 database')
    _log.info(_bank.list_collection_names())
    _bank.users.drop()
    _bank.loans.drop()
    _bank.counter.drop()

    _bank.counter.insert_one({'_id': 'UNIQUE_COUNT', 'count': 0})

    user_list = []
    user_list.append(User(_get_id(), 'mm', '11', 'matt', 'matt', 'customer').to_dict())
    user_list.append(User(_get_id(), 'dd', '22', 'david', 'davies', 'customer').to_dict())
    user_list.append(User(_get_id(), 'ff', '33', 'fan', 'fan', 'manager').to_dict())

    _bank.users.insert_many(user_list)
    _bank.users.application_info.create_index('ssn', unique=True)
    _bank.users.create_index('username', unique=True)
