from django.urls import resolve, reverse
from django.test import TestCase
from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home_page)