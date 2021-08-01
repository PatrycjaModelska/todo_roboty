from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

from unittest import skip


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edyta przeszła na stronę główną i przypadkowo spróbowała utworzyć
        # pusty element na liście. Nacisnęła klawisz Enter w pustym polu tekstowym.
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Po odświeżeniu strony głównej zobaczyła komunikat błędu
        # informujący o niemożliwości utworzenia pustego elementu na liście.
        import time
        time.sleep(3)
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "Element nie może być pusty")

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
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "Element nie może być pusty")

        # Element mogła poprawić, wpisując w nim dowolny tekst.
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Zrobić herbatę')
        inputbox.send_keys(Keys.ENTER)
        import time
        time.sleep(3)
        self.check_for_row_in_list_table('1: Kupić mleko')
        self.check_for_row_in_list_table('2: Zrobić herbatę')
