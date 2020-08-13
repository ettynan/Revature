'''Module to test the project2.SchoolSystem.schedules.model module'''
import unittest

from SchoolSystem.schedules.model import Schedule

from SchoolSystem.data.logger import get_logger

_log = get_logger(__name__)

class ScheduleTestSuite(unittest.TestCase):
    '''Test suite for User Class'''
    schedule = None
    def setUp(self):
        self.schedule = Schedule(-1, 'jill', {'class1', 'class2', 'class3',
                                 'class4', 'class5'})
    def tearDown(self):
        self.schedule = None
    @classmethod
    def setUpClass(cls):
        cls.schedule = Schedule()
    @classmethod
    def tearDownClass(cls):
        cls.schedule = None

    def test_get_id(self):
        '''Tests retrieval of get_id'''
        _log.info('Testing test_get_id')
        self.assertEqual(-1, ScheduleTestSuite.schedule.get_id())

    def test_set_id(self):
        '''Tests to see if set_id works'''
        _log.info('Testing test_set_id')
        ScheduleTestSuite.schedule.set_id(-10)
        self.assertEqual(-10, ScheduleTestSuite.schedule._id)

    def test_str(self):
        '''Tests __str__ in schedule'''
        _log.info('Testing test_str')
        self.schedule = Schedule('username', {'class1', 'class2', 'class3',
                                 'class4', 'class5'})
        self.assertIs(type(str(ScheduleTestSuite.schedule)), str)

    def test_to_dict(self):
        '''Test to_dict in schedule'''
        _log.info('Testing test_to_dict')
        self.user = Schedule('username', 'password')
        self.assertIs(type(ScheduleTestSuite.schedule.to_dict()), dict)

    def test_from_dict(self):
        '''Test from_dict in schedule'''
        _log.info('Testing test_from')
        test_dict = {'username': 'username', 'schedule' :{'class1', 'class2',
                     'class3', 'class4', 'class5'}}
        self.schedule = Schedule().from_dict(test_dict)
        self.assertIs(type(ScheduleTestSuite.schedule), Schedule)



if __name__ == '__main__':
    unittest.main()
