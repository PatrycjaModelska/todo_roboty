from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve, reverse
from django.template.loader import render_to_string
import re
from lists.views import home_page

def remove_csrf_tag(text):
    """Remove csrf tag from TEXT"""
    return re.sub(r'<[^>]*csrfmiddlewaretoken[^>]*>', '', text)

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)

        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        # print(expected_html)
        # print(remove_csrf_tag(response.content.decode()))
        self.assertEqual(remove_csrf_tag(response.content.decode()), expected_html)

        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>Listy rzeczy do zrobienia</title>', response.content)
        # self.assertTrue(response.content.strip().endswith(b'</html>'))

    def test_home_page_can_save_a_POST_request(self):
         request = HttpRequest()
         request.method = 'POST'
         request.POST['item_text'] = 'Nowy element listy'
         response = home_page(request)

         self.assertIn('Nowy element listy', response.content.decode())
         expected_html = render_to_string(
             'home.html',
             {'new_item_text': 'Nowy element listy'}
         )
         self.assertEqual(remove_csrf_tag(response.content.decode()), expected_html)


from lists.models import Item

class ItemModelTest(TestCase):
     def test_saving_and_retrieving_items(self):
         first_item = Item()
         first_item.text = 'Absolutnie pierwszy element listy'
         first_item.save()
         second_item = Item()
         second_item.text = 'Drugi element'
         second_item.save()
         saved_items = Item.objects.all()

         self.assertEqual(saved_items.count(), 2)
         first_saved_item = saved_items[0]
         second_saved_item = saved_items[1]
         self.assertEqual(first_saved_item.text, 'Absolutnie pierwszy element listy')
         self.assertEqual(second_saved_item.text, 'Drugi element')