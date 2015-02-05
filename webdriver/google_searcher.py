__author__ = 'user'

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class GoogleSearcher(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get('http://www.google.com.ar')

    def test_search_input_is_present(self):

        search_input = self.driver.find_element_by_name('q')
        assert search_input.is_displayed() is True

    def test_search_button_is_present(self):

        search_button = self.driver.find_element_by_name('btnK')
        assert search_button.is_displayed() is True

    def test_basic_search(self):
        search_input = self.driver.find_element_by_name('q')
        search_input.send_keys('Globallogic Argentina')
        search_input.submit()
        search_result = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="rso"]/div[2]/li[1]/div/h3/a)')
        )
        assert search_result.text == 'Globallogic | Innovation by design'

    def tearDown(self):
        self.driver.quit()