from django.test import SimpleTestCase
from myapp1.views import index,home
from django.urls import reverse,resolve


class  TestUrls(SimpleTestCase):

    def test_index_url(self):
        url = reverse("index")
        # print(url)
        # print(resolve(url))
        self.assertEqual(resolve(url).func,index)

    def test_home_url(self):
        url = reverse("home")
        # print(url)
        # print(resolve(url))
        self.assertEqual(resolve(url).func,home)

