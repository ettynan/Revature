'''Module to test the project0.users.model module'''
import unittest

from project0.users.model import User
from project0.vehicles.model import Vehicle

from project0.data.logger import get_logger

_log = get_logger(__name__)

#Unit Test Suite
class UserTestSuite(unittest.TestCase):
    '''Test suite for User Class'''
    user = None
    def setUp(self):
        self.user = User(-1, 'jill', '111', 'jill', 'mill', 'customer')
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
        print('Testing get id')
        self.assertEqual(UserTestSuite.user.get_id(), -1)

    def test_get_payments(self):
        '''Method tests if payments of vehicle is returned'''
        _log.info('Testing test_get_payments')
        print('Testing get payments')
        UserTestSuite.user.payments = [200.00, 300.00]
        self.assertIs(UserTestSuite.user.get_payments(), UserTestSuite.user.payments)

    def test_get_role(self):
        '''Tests retrieval of get_role'''
        _log.info('Testing test_get_role')
        print('Testing get role')
        UserTestSuite.user.role = 'customer'
        self.assertEqual(UserTestSuite.user.get_role(), 'customer')

    def test_get_owned_vehicles(self):
        '''Tests retrieval of get_owned_vehicles'''
        _log.info('Testing test_owned_vehicles')
        print('Testing get owned vehicles')
        vehicle = Vehicle(1, 'blah', 'blah', 'blah', 'blah', 0.0)
        UserTestSuite.user.owned_vehicles = vehicle
        self.assertEqual(UserTestSuite.user.get_owned_vehicles(), vehicle)

    def test_add_vehicle_owned(self):
        '''Tests setting of add_vehicle_owned'''
        _log.info('Testing test_add_vehicle_owned')
        print('Testing add vehicle owned')
        vehicle_id = 1
        UserTestSuite.user.add_vehicle_owned(vehicle_id)
        self.assertIsNone(UserTestSuite.user.add_vehicle_owned(vehicle_id))

if __name__ == '__main__':
    unittest.main()