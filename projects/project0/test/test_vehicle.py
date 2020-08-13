'''Module to test the project0.users.model module'''
import unittest

from project0.vehicles.model import Vehicle
from project0.users.model import User
from project0.offers.model import Offer
from project0.data.logger import get_logger

_log = get_logger(__name__)

#Unit Test Suite
class VehicleTestSuite(unittest.TestCase):
    '''Test suite for Vehicle Class'''
    vehicle = None
    def setUp(self):
        '''Method runs before every test'''
        VehicleTestSuite.vehicle = Vehicle(1, 'blah', 'blah', 'blah', 'blah', 0.0)

    def tearDown(self):
        '''This method runs after each test to reset'''
        VehicleTestSuite.vehicle = None

    @classmethod
    def setUpClass(cls):
        '''Method runs before any test'''
        cls.user = User()

    @classmethod
    def tearDownClass(cls):
        '''Method runs after every test'''
        cls.user = None

    def test_get_id(self):
        '''Tests retrieval of get_id'''
        _log.info('Testing test_get_get')
        print('Testing get id')
        self.assertEqual(VehicleTestSuite.vehicle.get_id(), 1)

    def test_is_available(self):
        '''Method tests if vehicle already owned'''
        _log.info('Testing test_is_available')
        print('Testing is available')
        self.assertTrue(VehicleTestSuite.vehicle.is_available(), "Should be true")

    def test_get_owner(self):
        '''Method tests if owner of vehicle is returned'''
        _log.info('Testing test_get_owner')
        print('Testing get owner')
        VehicleTestSuite.vehicle.owner = 20
        self.assertIs(VehicleTestSuite.vehicle.get_owner(), 20)

    def test_get_offers(self):
        '''Tests offers list is returned'''
        '''Method tests if offers on vehicle is returned'''
        _log.info('Testing test_get_offers')
        VehicleTestSuite.offer = Offer(2, 1.0, -1, -1)
        VehicleTestSuite.vehicle.offers.append(VehicleTestSuite.offer)
        offers = VehicleTestSuite.vehicle.get_offers()
        self.assertEqual(offers[0], VehicleTestSuite.offer)

if __name__ == '__main__':
    unittest.main()
