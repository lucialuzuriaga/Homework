__author__ = 'user'

import unittest
from core.test_suite import TestSuite


class TestTestSuite(unittest.TestCase):

    def setUp(self):
        self.test_suite = TestSuite()
        self.test_suite.add_test('successful login')

    def test_add_test(self):
        current_tests = self.test_suite.get_contained_tests()

        self.assertEqual(1, current_tests)

    def test_add_test_empty_name(self):
        self.test_suite.add_test(None)

        current_tests = self.test_suite.get_contained_tests()

        self.assertEqual(1, current_tests)

    def test_remove_test(self):
        self.test_suite.remove_test()
        current_tests = self.test_suite.get_contained_tests()

        self.assertEqual(0, current_tests)


if __name__ == '__main__':
    unittest.main()
