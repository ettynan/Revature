'''Modularization of Mongo data access
    Define all of our CRUD (Create, Read, Update, and Delete)
    in this file  to separate those concerns'''

import os
import sys
import getpass
import pymongo

from project0.users.model import User
from project0.vehicles.model import Vehicle
from project0.data.logger import get_logger

_log = get_logger(__name__)

try:
    _car = pymongo.MongoClient(os.environ.get('MONGO_URI')).project0
except:
    _log.exception('Could not connect to Mongo')
    raise

#CRUD operations for database
def get_vehicles():
    '''Read all vehicles from the collection'''
    dict_list = _car.vehicles.find()
    return [Vehicle.from_dict(vehicle) for vehicle in dict_list]

# combine to get_item_by_id
def get_vehicles_by_id(item_id):
    '''Returns vehicle by its id'''
    _log.info('Attempting to retrieve vehicles matching owner from database')
    query = {'_id': item_id}
    vehicle_dict = _car.vehicles.find_one(query)
    return Vehicle.from_dict(vehicle_dict) if vehicle_dict else None

def get_all_payments():
    '''Returns a list of all payments'''
    query = {'owner': {'$ne': None}}
    return [Vehicle.from_dict(vehicle) for vehicle in _car.vehicles.find(query)]

def get_user_by_id(item_id):
    '''Returns the user_by user id'''
    _log.info('Attempting to retrieve user from database')
    query = {'_id': item_id}
    user = _car.users.find_one(query)
    return User.from_dict(user) if user else None

def get_available_vehicles():
    '''Returns cars not owned by any customers'''
    query = {'owner': {'$eq': None}}
    return [Vehicle.from_dict(vehicle) for vehicle in _car.vehicles.find(query)]

def delete_item(item_type, item):
    '''Removes an item from the database'''
    _log.debug(type(item).__name__)
    if item_type == 'Vehicle':
        query = {'_id': item.get_id()}
        _car.vehicles.delete_one(query)
    else:
        print('Invalid selection.')

def login_mongo(username, password):
    '''A function that takes in a username and password and returns user object'''
    _log.info('\nAttempting to retrieve user from database')
    query_dict = {'username': username, 'password': password}
    user_dict = _car.users.find_one(query_dict)
    return User.from_dict(user_dict) if user_dict else None

def get_user_info():
    '''Returns a username'''
    username = input('Enter username or q to quit: ')
    if username == 'q':
        sys.exit()
    password = getpass.getpass('Input password (q to quit): ')
    if password == 'q':
        sys.exit()
    return

def insert_item(item):
    '''Inserts a new user chosen item into the database'''
    item_type = type(item).__name__
    item._id = _get_id()
    if item_type == 'User':
        user = item
        user._id = item._id
        _car.users.insert_one(user.to_dict())
    elif item_type == 'Vehicle':
        vehicle = item
        vehicle._id = item._id
        _car.vehicles.insert_one(vehicle.to_dict())
    else:
        print('invalid')

def insert_item_offer(item, vehicle=None):
    '''Adds an offer to a vehicle'''
    item_type = type(item).__name__
    item._id = _get_id()
    if item_type == 'Offer':
        offers = item
        query = {'_id': vehicle.get_id()}
        push = {'$push': {'offers': offers.to_dict()}}
        _car.vehicles.find_one_and_update(query, push)

def _get_id():
    '''Retrieves the next id in the database and increments it'''
    return _car.counter.find_one_and_update({'_id': 'UNIQUE_COUNT'},
                                            {'$inc': {'count': 1}},
                                            return_document=pymongo.ReturnDocument.AFTER)['count']
def update_user(user: User):
    '''Updates the user to owner if offer accepted and vehicle owner to user'''
    try:
        query = {'_id': user.get_id()}
        _car.users.update_one(query, {'$set': user.to_dict()})
    except:
        _log.exception('Could not update user')
        raise

def update_offer(vehicle: Vehicle):
    '''Updates the database on the new offer status based on vehicle id'''
    try:
        query = {'_id':  vehicle.get_id()}
        _car.vehicles.update_one(query, {'$set': vehicle.to_dict()})
    except:
        _log.exception('Could not update offer')
        raise

if __name__ == '__main__':
    _log.info('Running Mongo script: dropping collections from project0 database')
    _log.info(_car.list_collection_names())
    _car.users.drop()
    _car.vehicles.drop()
    _car.offers.drop()
    _car.counter.drop()

    _car.counter.insert_one({'_id': 'UNIQUE_COUNT', 'count': 0})

    user_list = []
    user_list.append(User(_get_id(), 'msmith', '111', 'Matthew', 'Smith',
                          'employee').to_dict())
    user_list.append(User(_get_id(), 'wjames', '222', 'William', 'James',
                          'employee').to_dict())
    user_list.append(User(_get_id(), 'jjones', '333', 'Justin', 'Jones',
                          'employee').to_dict())

    user_list.append(User(_get_id(), 'vsaller', '444', 'Victoria', 'Saller',
                          'customer').to_dict())
    user_list.append(User(_get_id(), 'jijones', '555', 'Jimmy', 'Jones',
                          'customer').to_dict())
    user_list.append(User(_get_id(), 'ssight', '666', 'Sally', 'Sight',
                          'customer').to_dict())

    vehicle_list = []
    vehicle_list.append(Vehicle(_get_id(), 'Honda', 'Civic', '2003',
                                'tan', 3400.00).to_dict())
    vehicle_list.append(Vehicle(_get_id(), 'Toyota', 'Tercel', '2013',
                                'black', 7395.00).to_dict())
    vehicle_list.append(Vehicle(_get_id(), 'Subaru', 'Forrester', '2019',
                                'green', 24399.00).to_dict())

    _car.users.insert_many(user_list)
    _car.users.create_index('username', unique=True)
    _car.vehicles.insert_many(vehicle_list)
