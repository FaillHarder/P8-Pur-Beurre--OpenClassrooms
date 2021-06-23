from django import forms
from django import forms
from django.forms.widgets import PasswordInput

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=50, label="Username")
    password = forms.CharField(max_length=50, label="Password", widget=PasswordInput)
    email = forms.EmailField(max_length=100, label="Email")
    first_name = forms.CharField(max_length=50, label="First Name")
    last_name = forms.CharField(max_length=50, label="Last Name")