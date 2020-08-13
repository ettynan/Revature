'''Module to test the project0.offers.model module'''
import unittest

from project0.vehicles.model import Vehicle
from project0.users.model import User
from project0.offers.model import Offer
from project0.data.logger import get_logger


_log = get_logger(__name__)

#Unit Test Suite
class OfferTestSuite(unittest.TestCase):
    '''Test suite for Offer Class'''
    offer = None
    def setUp(self):
        '''Method runs before every test'''
        OfferTestSuite.offer = Offer(1, 'pending', 400.0, 10)

    def tearDown(self):
        '''Method runs after each test to reset'''
        OfferTestSuite.offer = None

    @classmethod
    def setUpClass(cls):
        '''Method runs before any test'''
        cls.user = User()

    @classmethod
    def tearDownClass(cls):
        '''Method runs after every test'''
        cls.user = None

    def test_get_offer_amount(self):
        '''Tests return of get_offer_amount'''
        _log.info('Testing test_get_offer_amount')
        print('Testing get offer amount')
        self.assertEqual(OfferTestSuite.offer.get_offer_amount(), OfferTestSuite.offer.offer_amount)

    def test_get_status(self):
        '''Tests return of get_status'''
        _log.info('Testing test_get_status')
        print('Testing get status')
        self.assertEqual(OfferTestSuite.offer.get_status(), OfferTestSuite.offer.status)

    def test_set_status(self):
        '''Tests return of set status'''
        _log.info('Testing test_set status')
        print('Testing set status')
        OfferTestSuite.offer.set_status('rejected')
        self.assertIs(OfferTestSuite.offer.status, 'rejected')

    def test_get_customer_id(self):
        '''Tests return of get customer id'''
        _log.info('Testing test_customer_id')
        print('Testing get customer id')
        self.assertEqual(OfferTestSuite.offer.get_customer_id(), OfferTestSuite.offer.customer_id)



if __name__ == '__main__':
    unittest.main()