from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
import datetime
from django.utils import timezone
from PIL import Image


class AdditionalEquipment(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Engine(models.Model):
    name = models.CharField(max_length=200)
    power = models.FloatField(default=0)
    consummation = models.FloatField(default=0)

    def __str__(self):
        return self.name

class FuelType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ModelOfCar(models.Model):
    name = models.CharField(max_length=200)
    modelImg=models.ImageField(upload_to='car_pictures/',default='/static/car/car-default.jpg')
    def __str__(self):
        return self.name

class Gallery(models.Model):
    userImg = models.ImageField(upload_to='car_pictures/', default='NULL')

class City(models.Model):
    name = models.CharField(max_length=200)
    map_link = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class BankCard(models.Model):
    full_name = models.CharField(max_length=64)
    card_numbers = models.CharField(max_length=16)
    expiration_month = models.CharField(max_length=10, null=True)
    expiration_year = models.CharField(max_length=4, null=True)
    cvv_code = models.CharField(max_length=4)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name


class DriverLicense(models.Model):
    license_picture = models.ImageField(upload_to='license_pictures/', default='NULL')

class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name

class Car(models.Model):
    name = models.CharField(max_length=200)
    model_id = models.ForeignKey(ModelOfCar, on_delete=models.CASCADE, default=1)
    model_year = models.IntegerField()
    price_hourly = models.FloatField()
    start_date = models.DateTimeField('starting date',null=True, blank=True)
    end_date = models.DateTimeField('ending date',null=True, blank=True)
    available = models.BooleanField()
    rate = models.IntegerField(default=0)
    engine_id = models.ForeignKey(Engine, on_delete=models.CASCADE,default=1)
    fuel_id = models.ForeignKey(FuelType, on_delete=models.CASCADE,default=1)
    picture_id = models.ForeignKey(Gallery, on_delete=models.CASCADE,default=1)
    add_equip_id = models.ForeignKey(AdditionalEquipment, on_delete=models.CASCADE,default=1)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.name

    class Meta:
        ordering=['rate']


class SimpleUser(AbstractUser):
    birth_date = models.DateTimeField('date of birth', null=True, blank=True)
    address = models.CharField(default='NULL',max_length=200)
    userImg = models.ImageField(upload_to='user_avas/', default='user_avas/default.jpg')
    bank_card_id = models.ForeignKey(BankCard, on_delete=models.PROTECT, default=1)
    license_id = models.ForeignKey(DriverLicense, on_delete=models.PROTECT, default=1)

    def was_born_date(self):
        return self.birth_date >= timezone.now() - datetime.timedelta(days=1)

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.userImg.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.userImg.path)


class Order(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, default=0)
    user_id = models.ForeignKey(SimpleUser, on_delete=models.CASCADE, default=0)
    approves = models.BooleanField()
    finished = models.BooleanField()
    canceled = models.BooleanField()
    total_price = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    bank_card_id = models.ForeignKey(BankCard, on_delete=models.PROTECT, default=1)
    license_id = models.ForeignKey(DriverLicense, on_delete=models.PROTECT, default=1)
    email_address = models.EmailField(max_length=20, null=True)
