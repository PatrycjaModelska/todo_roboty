from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve, reverse
from django.template.loader import render_to_string

from lists.views import home_page


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
        self.assertEqual(response.content.decode(), expected_html)

        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>Listy rzeczy do zrobienia</title>', response.content)
        # self.assertTrue(response.content.strip().endswith(b'</html>'))

