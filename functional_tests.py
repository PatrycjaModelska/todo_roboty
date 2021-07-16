import unittest
from selenium import webdriver


class DjangoReadyToWorkTestCase(unittest.TestCase):
    def test_check_browser_title(self):
        browser = webdriver.Firefox()
        browser.get('http://127.0.0.1:8000')
        self.assertEqual(browser.title, 'The install worked successfully! Congratulations!')
