from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
import datetime
from django.utils import timezone

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

    def __str__(self):
        return self.name

class Gallery(models.Model):
    userImg = models.ImageField(upload_to='car_pictures/', default='NULL')


class Car(models.Model):
    name = models.CharField(max_length=200)
    model_id = models.ForeignKey(ModelOfCar, on_delete=models.CASCADE, default=1)
    model_year = models.IntegerField()
    price_hourly = models.FloatField()
    available = models.BooleanField()
    rate = models.IntegerField(default=0)
    engine_id = models.ForeignKey(Engine, on_delete=models.CASCADE,default=1)
    fuel_id = models.ForeignKey(FuelType, on_delete=models.CASCADE,default=1)
    picture_id = models.ForeignKey(Gallery, on_delete=models.CASCADE,default=1)
    add_equip_id = models.ForeignKey(AdditionalEquipment, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name

class Order(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, default=0)
    start_date = models.DateTimeField('starting date')
    end_date = models.DateTimeField('ending date')
    approves = models.BooleanField()
    finished = models.BooleanField()
    canceled = models.BooleanField()
    total_price = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)



class SimpleUser(AbstractUser):
    birth_date = models.DateTimeField('date of birth', null=True, blank=True)
    address = models.CharField(default='NULL',max_length=200)
    userImg = models.ImageField(upload_to='user_avas/', default='NULL')

    def was_born_date(self):
        return self.birth_date >= timezone.now() - datetime.timedelta(days=1)
