'''Module to test the project2.SchoolSystem.users.model module'''
import unittest

from SchoolSystem.users.model import User

from SchoolSystem.data.logger import get_logger

_log = get_logger(__name__)

class UserTestSuite(unittest.TestCase):
    '''Test suite for User Class'''
    user = None
    def setUp(self):
        self.user = User(-1, 'jill', '111', 'jill', 'mill', 'Customer')
    def tearDown(self):
        self.user = None
    @classmethod
    def setUpClass(cls):
        cls.user = User()
    @classmethod
    def tearDownClass(cls):
        cls.user = None

    def test_get_id(self):
        '''Tests retrieval of get_id'''
        _log.info('Testing test_get_id')
        self.assertEqual(-1, UserTestSuite.user.get_id())

    def test_set_id(self):
        '''Tests to see if set_id works'''
        _log.info('Testing test_set_id')
        UserTestSuite.user.set_id(-10)
        self.assertEqual(-10, UserTestSuite.user._id)

    def test_str(self):
        '''Tests __str__ in user'''
        _log.info('Testing test_str')
        self.user = User('username', 'password', 'firstname', 'lastname')
        self.assertIs(type(str(UserTestSuite.user)), str)

    def test_to_dict(self):
        '''Test to_dict in user'''
        _log.info('Testing test_to_dict')
        self.user = User('username', 'password')
        self.assertIs(type(UserTestSuite.user.to_dict()), dict)

    def test_from_dict(self):
        '''Test from_dict in user'''
        _log.info('Testing test_from')
        test_dict = {'username': 'username', 'password': 'password',
                     'firstname': 'firstname', 'lastname': 'lastname'}
        self.user = User().from_dict(test_dict)
        self.assertIs(type(UserTestSuite.user), User)



if __name__ == '__main__':
    unittest.main()
