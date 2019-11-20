from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
# Create your views here.

def index(request):
    return render(request,'ourApp/index2.html')

def about(request):
    return render(request,'ourApp/about.html')

def get_by_id(request, car_id):
    return HttpResponse(Car.objects.get(id=car_id))

def services(request):
    return render(request,'ourApp/services.html')

def cars(request):
    return render(request,'ourApp/car-without-sidebar.html')

def contact(request):
    return render(request,'ourApp/car-without-sidebar.html')
