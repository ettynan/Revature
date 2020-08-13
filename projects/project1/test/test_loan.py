'''Module to test the project1.loans.model module'''
import unittest

from project1.users.model import User
from project1.loans.model import Loan

from project1.data.logger import get_logger

_log = get_logger(__name__)


class LoanTestSuite(unittest.TestCase):
    '''Test suite for Loan class'''
    loan = None
    def setUp(self):
        self.loan = Loan('Mortgage')
        self.loan = Loan('Car')
        self.loan = Loan('Student')
        self.loan = Loan('Personal')
    def tearDown(self):
        self.loan = None
    @classmethod
    def setUpClass(cls):
        cls.loan = Loan()
    @classmethod
    def tearDownClass(cls):
        cls.loan = None

    def test_set_cosigner_needed(self):
        '''Tests to see if set_cosigner_needed works'''
        _log.info('Testing set_cosigner_needed')
        LoanTestSuite.loan.set_cosigner_needed('Required')
        self.assertEqual('Required', LoanTestSuite.loan.cosigner_needed)

    def test_set_collateral_needed(self):
        '''Tests to see if set_collateral_needed works'''
        _log.info('Testing set_collateral_needed')
        LoanTestSuite.loan.set_collateral_needed('Required')
        self.assertEqual('Required', LoanTestSuite.loan.collateral_needed)

    def test_set_risk_score(self):
        '''Tests to see if set_risk_score works'''
        _log.info('Testing set_risk_score')
        LoanTestSuite.loan.set_risk_score(1.45)
        self.assertEqual(1.45, LoanTestSuite.loan.risk_score)

    def test_set_credit_score(self):
        '''Tests to see if set_credit_score works'''
        _log.info('Testing set_credit_score')
        LoanTestSuite.loan.set_credit_score(600)
        self.assertEqual(600, LoanTestSuite.loan.credit_score)

    def test_set_status(self):
        '''Tests to see if set_status works'''
        _log.info('Testing set_status')
        LoanTestSuite.loan.set_status('Approved')
        self.assertEqual('Approved', LoanTestSuite.loan.status)

    def test_str(self):
        '''Test __str__ in loan'''
        _log.info('Testing __st__ in loan')
        self.loan = Loan('Car')
        self.assertIs(type(str(LoanTestSuite.loan)), str)

    def test_to_dict(self):
        '''Test to_dict in loan'''
        _log.info('Testing to_dict')
        self.loan = Loan('Mortgage')
        self.assertIs(type(LoanTestSuite.loan.to_dict()), dict)

    def test_from_dict(self):
        '''Test from_dict in loan'''
        _log.info('Testing from_dict')
        test_dict = {'loan_type': 'Personal'}
        self.loan = Loan().from_dict(test_dict)
        self.assertIs(type(LoanTestSuite.loan), Loan)

    def test_get_collateral_needed(self):
        '''Tests retrieval of get_collateral_needed'''
        _log.info('Testing test_get_collateral_needed')
        LoanTestSuite.loan.collateral_needed = 'Required'
        self.assertEqual(LoanTestSuite.loan.get_collateral_needed(),
                         LoanTestSuite.loan.collateral_needed)

if __name__ == '__main__':
    unittest.main()