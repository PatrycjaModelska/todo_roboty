import unittest
from selenium import webdriver


class DjangoReadyToWorkTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get('http://127.0.0.1:8000')

    def test_check_browser_title(self):
        self.assertEqual(self.browser.title, 'The install worked successfully! Congratulations!')

    def test_can_start_a_list_and_retrieve_it_later(self):
         self.assertIn('Listy', self.browser.title)
         self.fail('Zakończenie testu!')

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
