from django.test import TestCase,Client
from django.urls import reverse

class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass
    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        self.client = Client()
    def test_index_view(self):
        
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'myapp1/index.html')

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'myapp1/home.html')
