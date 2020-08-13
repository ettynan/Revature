'''Module to test the project1.users.model module'''
import unittest

from project1.users.model import User, ApplicationInfo
# from project1.loans.model import Loan

from project1.data.logger import get_logger

_log = get_logger(__name__)

#Unit Test Suite
class ApplicationInfoTestSuite(unittest.TestCase):
    '''Test suite for ApplicationInfo Class'''
    application = None
    def setUp(self):
        self.application = ApplicationInfo('Uname', 'First Name',' Last Name',
                                           '34', 'Gender', '456789345', 'Title',
                                           'Employer', '123333', '1233',
                                           '1 Dravus', 'Seattle', 'WA', '98109',
                                           '1 Dravus', 'Seattle', 'WA', '98109')
    def tearDown(self):
        self.application = None
    @classmethod
    def setUpClass(cls):
        cls.application = ApplicationInfo()
    @classmethod
    def tearDownClass(cls):
        cls.application = None

    def test_to_dict(self):
        '''Testing to_dict for application info'''
        self.application = ApplicationInfo('Uname', 'First Name', 'Last Name',
                                           '34', 'Gender', '456789345', 'Title',
                                           'Employer', '123333', 1233,
                                           '1 Dravus', 'Seattle', 'WA', '98109',
                                           '1 Dravus', 'Seattle', 'WA', '98109')
        self.assertIs(type(ApplicationInfoTestSuite.application.to_dict()), dict)

    def test_from_dict(self):
        '''Test from_dict for application info'''
        test_dict = {'username': 'Username', 'age': '34', 'gender': 'fluid',
                     'ssn': '456789345', 'title': 'awesome',
                     'employer': 'the man', 'salary': '123333',
                     'expenses': 1233, 'b_street': '1 Dravus',
                     'b_city': 'Seattle', 'b_state': 'WA',
                     'b_zip': '98109', 'm_street': '1 Dravus',
                     'm_city': 'Seattle', 'm_state': 'WA',
                     'm_zip': '98109'}

        self.application = ApplicationInfo().from_dict(test_dict)
        self.assertIs(type(ApplicationInfoTestSuite.application),
                      ApplicationInfo)

    def test_str(self):
        '''Tests __str__ in applicationinfo'''
        _log.info('Testing test_str')
        self.application = ApplicationInfo('username')
        self.assertIs(type(str(ApplicationInfoTestSuite.application)), str)


if __name__ == '__main__':
    unittest.main()
