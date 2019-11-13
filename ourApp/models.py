from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=200)
    model_year = models.IntegerField()
    price_hourly = models.FloatField()
    available = models.BooleanField()
    rate = models.IntegerField(default=0)

    def __str__(self):
        return self.name
