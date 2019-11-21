from django import forms
from .models import SimpleUser
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(label='Your name', max_length=100)
    surname = forms.CharField(label='Your surname', max_length=100)


    class Meta:
        model = SimpleUser
        fields = ['username', 'name', 'surname', 'email', 'password1', 'password2']
