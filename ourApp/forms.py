from django import forms
from .models import SimpleUser, BankCard, DriverLicense, Contact, Order
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
    __MONTH_CHOICES = (
        (1, '01'),
        (2, '02'),
        (3, '03'),
        (4, '04'),
        (5, '05'),
        (6, '06'),
        (7, '07'),
        (8, '08'),
        (9, '09'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
    )

    __YEAR_CHOICES = (
        (2020, '2020'),
        (2021, '2021'),
        (2022, '2022'),
        (2023, '2023'),
        (2024, '2024'),
        (2025, '2025'),
        (2026, '2026'),
        (2027, '2027'),
        (2028, '2028'),
        (2029, '2029'),
        (2030, '2030'),
    )
    full_name = forms.CharField(max_length=64, label='Name as on card')
    card_numbers = forms.CharField(max_length=16, label='Credit Card Number')
    expiration_month = forms.ChoiceField(choices=__MONTH_CHOICES)
    expiration_year = forms.ChoiceField(choices=__YEAR_CHOICES)
    cvv_code = forms.CharField(max_length=4, label='CVV')
    country = forms.CharField(max_length=200)

    class Meta:
        model = BankCard
        fields = ['full_name', 'card_numbers', 'expiration_month', 'expiration_year', 'cvv_code', 'country']

    def save(self, commit=True):
        bank_card = super(BankCardForm, self).save(commit = False)
        bank_card.full_name = self.cleaned_data['full_name']
        bank_card.card_numbers = self.cleaned_data['card_numbers']
        bank_card.expiration_month = self.cleaned_data['expiration_month']
        bank_card.expiration_year = self.cleaned_data['expiration_year']
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

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email_address', 'website', 'subject', 'message']

    def save(self, commit=True):
        contact = super(ContactForm, self).save(commit = False)
        contact.full_name = self.cleaned_data['full_name']
        contact.email_address = self.cleaned_data['email_address']
        contact.website = self.cleaned_data['website']
        contact.subject = self.cleaned_data['subject']
        contact.message = self.cleaned_data['message']

        if commit:
            contact.save()

        return contact
