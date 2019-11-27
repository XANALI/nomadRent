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

    def save(self, commit = True):
        user = super(UserRegisterForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['name']
        user.last_name = self.cleaned_data['surname']

        if commit:
            user.save()

        return user
