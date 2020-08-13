'''This module starts the application'''
from project0.data.logger import get_logger
import project0.business.operations as ops
import project0.data.mongo as db
import pymongo

_log = get_logger(__name__)

person = None

while person is None:
    option = (input(' Select an option: 1. login, 2. register, 3. quit: '))
    if option == '3':
        break
    if option == '1':
        person = db.login_mongo()
        if person is None:
            print('Credentials not found, try again.')
        ops.enter_platform(person)
    elif option == '2':
        _log.info('\nAttempting to Register new user')
        try:
            ops.add_item('user')
        except pymongo.errors.DuplicateKeyError:
            _log.info('\nDuplicateKeyError - username already taken.')
            print('Username already taken, try again.')
        ops.enter_platform(person)
    else:
        print('not valid, try again')

print('Goodbye')
