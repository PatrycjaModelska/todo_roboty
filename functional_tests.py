from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import unittest


class DjangoReadyToWorkTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get('http://127.0.0.1:8000')

    # def test_check_browser_title(self):
    #     self.assertEqual(self.browser.title, 'The install worked successfully! Congratulations!')

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.assertIn('Listy', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Listy', header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Wpisz rzecz do zrobienia'
        )
        inputbox.send_keys('Kupić pawie pióra')
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Kupić pawie pióra' for row in rows)
        )
        self.fail('Zakończenie testu!')

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
