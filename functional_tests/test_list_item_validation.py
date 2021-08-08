import time

from selenium.common.exceptions import NoSuchElementException

from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edyta przeszła na stronę główną i przypadkowo spróbowała utworzyć
        # pusty element na liście. Nacisnęła klawisz Enter w pustym polu tekstowym.
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('')
        inputbox.send_keys(Keys.ENTER)

        # Po odświeżeniu strony głównej zobaczyła, że nie utworzył się żaden nowy element
        import time
        time.sleep(3)
        table = False
        try:
            table = self.browser.find_element_by_id('id_list_table')
        except NoSuchElementException:
            self.assertFalse(table)

        # Spróbowała ponownie, wpisując dowolny tekst, i wszystko zadziałało.
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Kupić mleko')
        inputbox.send_keys(Keys.ENTER)
        import time
        time.sleep(3)
        self.check_for_row_in_list_table('1: Kupić mleko')

        # Przekornie po raz drugi spróbowała utworzyć pusty element na liście.
        # Na stronie listy otrzymała ostrzeżenie podobne do wcześniejszego.
        self.get_item_input_box().send_keys(Keys.ENTER)
        import time
        time.sleep(3)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertNotIn('2: ', [row.text for row in rows])

        # Element mogła poprawić, wpisując w nim dowolny tekst.
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Zrobić herbatę')
        inputbox.send_keys(Keys.ENTER)
        import time
        time.sleep(3)
        self.check_for_row_in_list_table('1: Kupić mleko')
        self.check_for_row_in_list_table('2: Zrobić herbatę')

    def test_cannot_add_duplicate_items(self):
        # Edyta przeszła na stronę główną i zaczęła tworzyć nową listę.
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Kupić kalosze')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        self.check_for_row_in_list_table('1: Kupić kalosze')
        # Przypadkowo spróbowała wpisać element, który już znajdował się na liście.
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Kupić kalosze')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        # Otrzymała czytelny komunikat błędu.
        self.check_for_row_in_list_table('1: Kupić kalosze')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "Podany element już istnieje na liście.")