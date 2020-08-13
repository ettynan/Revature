''' A handler for User operations in our server '''
# External Modules
import json
from os import path
# Internal Modules
import project1.web.dispatch as dispatch
import project1.data.mongo as db
from project1.users.model import User, ItemEncoder
from project1.data.logger import get_logger

_log = get_logger(__name__)

class UserDispatcher(dispatch.Dispatcher):
    '''Customer Dispatcher for Users'''
    def dispatch(self, path: list, method, r_body=None):
        '''dispatch takes in a path and request body and
           returns status code and response body as tuple'''
        _log.debug(r_body)
        if method == 'GET':
            return self.get_operations(path)
        if method == 'POST':
            return self.post_operations(path, r_body)

    def get_operations(self, path: list):
        '''GET operations for user'''
        _log.debug('GET received on user dispatcher')
        #get to /users
        if len(path) == 1:
            _log.debug('path length')
            db_users_list = db.get_users()
            _log.debug(db_users_list)
            return (200, bytes(json.dumps(db_users_list, cls=ItemEncoder),
                               'utf-8'))

    def post_operations(self, path: list, r_body):
        '''POST operations for user'''
        _log.debug('POST request received')
        _log.debug(r_body)
        if len(path) == 1:
            r_body_temp = json.loads(r_body.decode('utf-8'))
            user = User.from_dict(r_body_temp)
            _log.debug(user)
            db.create_user(user)
            return (201, bytes(json.dumps(user, cls=ItemEncoder), 'utf-8'))
        if len(path) == 2:
            r_body_temp = json.loads(r_body.decode('utf-8'))
            user = db.login(r_body_temp['username'], r_body_temp['password'])
            if user:
                _log.info('Successful login from handler')
                value = bytes(json.dumps(user, cls=ItemEncoder), 'utf-8')
                return (200, value, 'json')
        return (401, b'Unauthorized')
