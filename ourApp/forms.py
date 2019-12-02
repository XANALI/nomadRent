from django import forms
from .models import SimpleUser, BankCard, DriverLicense
from django.contrib.auth.forms import UserCreationForm
from PIL import Image
import datetime

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

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    address = forms.CharField(label='Your address', max_length=100)

    class Meta:
        model = SimpleUser
        fields = ['username', 'first_name', 'last_name', 'email', 'address', 'userImg']

    def save(self, commit=True):
        user = super(UserUpdateForm, self).save(commit = False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.address = self.cleaned_data['address']
        user.userImg = self.cleaned_data['userImg']

        if commit:
            user.save()

        return user

class BankCardForm(forms.ModelForm):
    expire_date = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = BankCard
        fields = ['full_name', 'card_numbers', 'expire_date', 'cvv_code', 'country']

    def save(self, commit=True):
        bank_card = super(BankCardForm, self).save(commit = False)
        bank_card.full_name = self.cleaned_data['full_name']
        bank_card.card_numbers = self.cleaned_data['card_numbers']
        bank_card.expiration_date = self.cleaned_data['expire_date']
        bank_card.cvv_code = self.cleaned_data['cvv_code']
        bank_card.country = self.cleaned_data['country']

        if commit:
            bank_card.save()

        return bank_card

class DriverLicenseForm(forms.ModelForm):
    license_picture = forms.ImageField()

    class Meta:
        model = DriverLicense
        fields = ['license_picture']

    def save(self, commit=True):
        driver_license = super(DriverLicenseForm, self).save(commit = False)
        driver_license.license_picture = self.cleaned_data['license_picture']

        if commit:
            driver_license.save()

        return driver_license
