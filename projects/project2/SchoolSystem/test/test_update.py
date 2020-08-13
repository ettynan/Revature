'''Module to test the project2.SchoolSystem.updates.model module'''
import unittest

from SchoolSystem.updates.model import Update

from SchoolSystem.data.logger import get_logger

_log = get_logger(__name__)

class UpdateTestSuite(unittest.TestCase):
    '''Test suite for Update Class'''
    update = None
    def setUp(self):
        self.update = Update(-1, 'jill', {'info update - lots of info'})
    def tearDown(self):
        self.update = None
    @classmethod
    def setUpClass(cls):
        cls.update = Update()
    @classmethod
    def tearDownClass(cls):
        cls.update = None

    def test_get_id(self):
        '''Tests retrieval of get_id'''
        _log.info('Testing test_get_id')
        self.assertEqual(-1, UpdateTestSuite.update.get_id())

    def test_set_id(self):
        '''Tests to see if set_id works'''
        _log.info('Testing test_set_id')
        UpdateTestSuite.update.set_id(-10)
        self.assertEqual(-10, UpdateTestSuite.update._id)

    def test_str(self):
        '''Tests __str__ in update'''
        _log.info('Testing test_str')
        self.update = Update('username', {'update_info'})
        self.assertIs(type(str(UpdateTestSuite.update)), str)

    def test_to_dict(self):
        '''Test to_dict in update'''
        _log.info('Testing test_to_dict')
        self.update = Update('username', {'update_info'})
        self.assertIs(type(UpdateTestSuite.update.to_dict()), dict)

    def test_from_dict(self):
        '''Test from_dict in update'''
        _log.info('Testing test_from')
        test_dict = {'username': 'username', 'update_info': {'update_info'}}
        self.update = Update().from_dict(test_dict)
        self.assertIs(type(UpdateTestSuite.update), Update)



if __name__ == '__main__':
    unittest.main()
