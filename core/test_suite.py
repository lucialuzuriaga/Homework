__author__ = 'user'


class TestSuite():

    def __init__(self):
        self.__contained_tests = []

    def add_test(self, name):
        if name is not None:
            self.__contained_tests.append(name)

    def remove_test(self, name):
        self.__contained_tests.remove(name)

    def get_contained_tests(self):
        return self.__contained_tests