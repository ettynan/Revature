'''Testing suite for operations'''

import unittest
from unittest.mock import Mock
from project0.vehicles.model import Vehicle
from project0.users.model import User
from project0.offers.model import Offer
from project0.data.logger import get_logger
import project0.business.operations as ops

_log = get_logger(__name__)

class OperationsTestSuite(unittest.TestCase):
    mock = Mock()

    def test_accept_offer(self):
        _log.info('Testing test_accept_offer')
        print('Testing accept offer')
        user = User('jill', '111', 'jill', 'mill', 'customer')
        offer = Offer(1, 'pending', 400.0, 10)
        vehicle = Vehicle(1, 'honda', 'civic', '2003', 'tan', 0.0)
        offer_list = [offer]
        self.mock.ops.accept_helper(offer_list, 0)
        self.assertIsNotNone(ops.accept_helper(offer_list, 0))

    def test_monthly_payment_calc(self):
        '''Checks the monthly payment calc'''
        _log.info('Testing monthly_payment_calc')
        print('Testing monthly_payment_calc')
        vehicle = Vehicle(1, 'honda', 'civic', '2003', 'tan', 0.0)
        self.assertEqual(ops.monthly_payment_calc(1600, 16, vehicle), 100)
        self.assertEqual(ops.monthly_payment_calc(12000, 12, vehicle), 1000)

if __name__ == '__main__':
    unittest.main()