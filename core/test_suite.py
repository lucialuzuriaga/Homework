__author__ = 'user'


class TestSuite():

    def __init__(self):
        self.__contained_tests = 0

    def add_test(self, name):
        if name is not None:
            self.__contained_tests = self.__contained_tests + 1

    def remove_test(self):
        self.__contained_tests = self.__contained_tests - 1

    def get_contained_tests(self):
        return self.__contained_tests