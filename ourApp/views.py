from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Car, ModelOfCar
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    cars = Car.objects.all()
    models = ModelOfCar.objects.all()
    return render(request,'ourApp/index2.html',{'cars':cars,'models':models})

def about(request):
    return render(request,'ourApp/about.html')

def get_by_id(request, car_id):
    return HttpResponse(Car.objects.get(id=car_id))

def services(request):
    return render(request,'ourApp/services.html')

def cars(request):
    return render(request,'ourApp/car-without-sidebar.html')

def contact(request):
    return render(request,'ourApp/contact.html')

def login(request):
    return render(request,'ourApp/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request,'ourApp/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'ourApp/profile.html', {'user_form':form})

def order(request):
    return render(request,'ourApp/order.html')
