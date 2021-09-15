from django import forms
from myapp1.models import Product

# https://docs.djangoproject.com/en/3.2/topics/forms/

class UserInfoForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=10,required=True)
    your_age = forms.IntegerField(label='Your age',required=True)
    email = forms.EmailField(required=True)

class AddProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__' 