'''Module to test the project2.SchoolSystem.submissions.model module'''
import unittest

from SchoolSystem.submissions.model import Submission

from SchoolSystem.data.logger import get_logger

_log = get_logger(__name__)

class SubmissionTestSuite(unittest.TestCase):
    '''Test suite for Submission Class'''
    submission = None
    def setUp(self):
        self.submission = Submission(-1, 'jill', 'assignment1', 'Mr. Holland',
                                     'b', 'Content of content')
    def tearDown(self):
        self.submission = None
    @classmethod
    def setUpClass(cls):
        cls.submission = Submission()
    @classmethod
    def tearDownClass(cls):
        cls.submission = None

    def test_get_id(self):
        '''Tests retrieval of get_id'''
        _log.info('Testing test_get_id')
        self.assertEqual(-1, SubmissionTestSuite.submission.get_id())

    def test_set_id(self):
        '''Tests to see if set_id works'''
        _log.info('Testing test_set_id')
        SubmissionTestSuite.submission.set_id(-10)
        self.assertEqual(-10, SubmissionTestSuite.submission._id)

    def test_str(self):
        '''Tests __str__ in submission'''
        _log.info('Testing test_str')
        self.submission = Submission('student', 'assignment', 'teacher',
                                     'grade', 'content')
        self.assertIs(type(str(SubmissionTestSuite.submission)), str)

    def test_to_dict(self):
        '''Test to_dict in submission'''
        _log.info('Testing test_to_dict')
        self.submission = Submission('student', 'assignment', 'teacher',
                                     'grade', 'content')
        self.assertIs(type(SubmissionTestSuite.submission.to_dict()), dict)

    def test_from_dict(self):
        '''Test from_dict in submission'''
        _log.info('Testing test_from')
        test_dict = {'student': 'student', 'assignment': 'assignment',
                     'teacher': 'teacher', 'grade': 'grade',
                     'content': 'content'}
        self.submission = Submission().from_dict(test_dict)
        self.assertIs(type(SubmissionTestSuite.submission), Submission)



if __name__ == '__main__':
    unittest.main()
