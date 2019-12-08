from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import UserRegisterForm, UserUpdateForm, BankCardForm, DriverLicenseForm
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
# Create your views here.

def index(request):
    cars = Car.objects.all()
    models = ModelOfCar.objects.all()
    citys=City.objects.all()

    return render(request,'ourApp/index2.html',{'cars':cars,'models':models, 'citys':citys})

def about(request):
    return render(request,'ourApp/about.html')


def get_by_id(request, car_id):
    return HttpResponse(Car.objects.get(id=car_id))

def services(request):
    return render(request,'ourApp/services.html')

def cars(request):
    cars=Car.objects.all()
    paginator=Paginator(cars,2)
    page_number=request.GET.get('page',1)
    page=paginator.get_page(page_number)

    is_paginated=page.has_other_pages()

    if page.has_previous():
        prev_url='?page={}'.format(page.previous_page_number())
    else:
        prev_url=''

    if page.has_next():
        next_url='?page={}'.format(page.next_page_number())
    else:
        next_url=''

    context={
        'page_object':page,
        'is_paginated':is_paginated,
        'next_url':next_url,
        'prev_url':prev_url
    }

    return render(request,'ourApp/car-without-sidebar.html',context=context)

def contact(request):
    if request.method == 'POST':
        try:
            full_name = request.POST["full_name"]
            email = request.POST["email"]
            website = request.POST["website"]
            subject = request.POST["subject"]
            message = request.POST.get("review")

            contact = Contact(full_name=full_name, email_address=email, website=website, subject=subject, message=message)
            contact.save()
        except:
            print("message can't be send")
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
    cars=Car.objects.all()
    paginator=Paginator(cars,2)
    page_number=request.GET.get('page',1)
    page=paginator.get_page(page_number)
    citys=City.objects.all()
    location=''
    pickdate=''
    returndate=''

    is_paginated=page.has_other_pages()

    if page.has_previous():
        prev_url='?page={}'.format(page.previous_page_number())
    else:
        prev_url=''

    if page.has_next():
        next_url='?page={}'.format(page.next_page_number())
    else:
        next_url=''




    if request.method=="POST":
        try:
            location=request.POST['location']
            pickdate=request.POST['pickdate']
            returndate=request.POST['returndate']
            cars_location=Car.objects.filter(city_id=City.objects.get(name__icontains=location),available=True)
            #cars_location=Car.objects.filter(rate=5).delete()
            context={
                'cars':cars,
                'page_object':page,
                'is_paginated':is_paginated,
                'next_url':next_url,
                'prev_url':prev_url,
                'location':location,
                'pickdate':pickdate,
                'returndate':returndate,
                'citys':citys,
                'cars_location':cars_location,
                'order':order
            }
            return render(request,'ourApp/order.html',context=context)
        except:
            return render(request,'ourApp/order.html',{'Empty':"No cars in this location",'cars':cars,'citys':citys})
            print('the comments cannot be added')
    else:
        return render(request,'ourApp/order.html')

def convert(pickdate):
    step=1
    y=""
    m=""
    d=""
    for i in pickdate:
        if i!='/' and step==1:
            m=m+i
        elif i!='/' and step==2:
            d=d+i
        elif step==3:
            y=y+i
        else:
            step+=1
    return "%s-%s-%s"%(y,m,d)


def confirmation(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            bank_card_form = BankCardForm(request.POST, instance=request.user.bank_card_id)
            driver_license_form = DriverLicenseForm(request.POST, request.FILES, instance=request.user.license_id)
        else:
            bank_card_form = BankCardForm(request.POST)
            driver_license_form = DriverLicenseForm(request.POST, request.FILES)

        if bank_card_form.is_valid() and driver_license_form.is_valid():
            bank_card_form.save()
            driver_license_form.save()
            return redirect('index')

    else:
        if request.user.is_authenticated:
            bank_card_form = BankCardForm(instance=request.user.bank_card_id)
            driver_license_form = DriverLicenseForm(instance=request.user.license_id)
        else:
            bank_card_form = BankCardForm()
            driver_license_form = DriverLicenseForm()

    context = {
        'bank_card_form':bank_card_form,
        'driver_license_form':driver_license_form
    }
    return render(request,'ourApp/confirmation.html', context)
