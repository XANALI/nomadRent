from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
# Create your views here.

def index(request):
    return HttpResponse("Good day")

def get_by_id(request, car_id):
    return HttpResponse(Car.objects.get(id=car_id))
