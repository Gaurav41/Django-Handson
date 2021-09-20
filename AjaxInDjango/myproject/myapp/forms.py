from django import forms
from django.forms import fields
from .models import User

class UserRegistratation(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-contol','id':'nameid'}),
            'email':forms.EmailInput(attrs={'class':'form-contol','id':'emailid'}),
            'password':forms.PasswordInput(attrs={'class':'form-contol','id':'passwordid'}) 
        }