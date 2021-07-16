from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)

        self.assertIn('Listy', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Utwórz nową listę rzeczy do zrobienia', header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Wpisz rzecz do zrobienia'
        )
        inputbox.send_keys('Kupić pawie pióra')
        inputbox.send_keys(Keys.ENTER)

        import time
        time.sleep(2)

        edith_list_url = self.browser.current_url
        print(edith_list_url)
        self.assertRegex(edith_list_url, '/lists/.+')

        import time
        time.sleep(6)

        self.check_for_row_in_list_table('1: Kupić pawie pióra')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Użyć pawich piór do zrobienia przynęty')
        inputbox.send_keys(Keys.ENTER)

        import time
        time.sleep(6)

        self.check_for_row_in_list_table('1: Kupić pawie pióra')
        self.check_for_row_in_list_table('2: Użyć pawich piór do zrobienia przynęty')

        self.browser.quit()
        self.browser = webdriver.Firefox()
        # Franek odwiedza stronę główną.

        # Nie znajduje żadnych śladów listy Edyty.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Kupić pawie pióra', page_text)
        self.assertNotIn('zrobienia przynęty', page_text)
        # Franek tworzy nową listę, wprowadzając nowy element.
        # Jego lista jest mniej interesująca niż Edyty…
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Kupić mleko')
        inputbox.send_keys(Keys.ENTER)
        # Franek otrzymuje unikatowy adres URL prowadzący do listy.

        time.sleep(3)

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        # Ponownie nie ma żadnego śladu po liście Edyty.
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Kupić pawie pióra', page_text)
        self.assertIn('Kupić mleko', page_text)
        # Usatysfakcjonowani, oboje kładą się spać.



