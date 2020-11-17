from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    first_name = forms.CharField(label='Primeiro nome', max_length=100)
    last_name = forms.CharField(label='Sobrenome', max_length=100)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
