from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    msg1 = forms.CharField(widget=forms.Textarea)