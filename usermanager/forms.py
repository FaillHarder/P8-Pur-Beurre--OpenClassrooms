from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label='Prénom')
    last_name = forms.CharField(max_length=50, label='Nom')
    email = forms.EmailField(
        max_length=254,
        label='Email',
        help_text='Entrez une adresse mail valide'
    )
    username = forms.CharField(
        max_length=50,
        label='Nom d\'utilisateur',
        help_text='50 caractères maximum. Lettres, chiffres est @/./+/-/_ seulement',
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
