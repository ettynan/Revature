'''Unit testing for classes User, Application, and Loan'''
import unittest
import project1.business.bank_operations as ops
from project1.users.model import ApplicationInfo
from project1.loans.model import Loan
from project1.data.logger import get_logger

_log = get_logger(__name__)

class TestBankOperationsSuite(unittest.TestCase):
    '''Test suite for bank operations'''
    application1 = ApplicationInfo('Username','nile','barn', '34','Gender', '456789345',
                                  'Title', 'Employer', '123333', '1233', '1 Dravus', 'Seattle',
                                  'WA', '98109', '1 Dravus', 'Seattle', 'WA', '98109')
    loan = Loan('Personal')

    def test_cal_risk_score(self):
        '''Test the calc_risk_score function'''
        _log.info('Testing cal_risk_score')
        self.assertEqual(1.95, ops.cal_risk_score(TestBankOperationsSuite.application1))
        application = ApplicationInfo('zz','First Name','Last Name', '34','Gender', '456789345',
                                      'Title', 'Employer', '123333', '1233', '1 Dravus', 'Seattle',
                                      'WA', '98109', '1 Dravus', 'Seattle', 'WA', '98109')
        self.assertEqual(1.45, ops.cal_risk_score(application))

    def test_credit_score(self):
        '''Test the calc_credit_score function'''
        _log.info('Testing credit_score')
        self.assertEqual(320, ops.credit_score(TestBankOperationsSuite.application1))
        application = ApplicationInfo('aa','First Name','Last Name', '34','Gender', '456789345',
                                      'Title', 'Employer', '123333', '1233', '1 Dravus', 'Seattle',
                                      'WA', '98109', '1 Dravus', 'Seattle', 'WA', '98109')
        self.assertEqual(600, ops.credit_score(application))

if __name__ == '__main__':
    unittest.main()