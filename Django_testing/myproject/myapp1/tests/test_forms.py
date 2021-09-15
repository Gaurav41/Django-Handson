from django.test import TestCase
from myapp1.forms import UserInfoForm,AddProductForm

class TestForms(TestCase):

    def test_add_product_form_valid_data(self):
        form = AddProductForm(data={
            'name': "iphone 13", 
            'description': "Brand New Apple Iphone 13", 
            'quantity':'1','price_per_item':"100000000"}
                )
        self.assertTrue(form.is_valid())

    def test_add_product_form_no_data(self):
        form = AddProductForm(data={})
        self.assertFalse(form.is_valid())

    def test_user_info_form_valid_data(self):
        form = UserInfoForm(data={"your_name":"Gaurav",
        "your_age":22,
        "email":"asd@gmail.com"})     
        self.assertTrue(form.is_valid())

    def test_user_info_form_no_data(self):
        form = UserInfoForm(data={})     
        self.assertFalse(form.is_valid())
