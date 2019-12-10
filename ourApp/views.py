from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import UserRegisterForm, UserUpdateForm, BankCardForm, DriverLicenseForm, ContactForm
from django.contrib.auth.decorators import login_required
from carRental.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime, date, time
# Create your views here.

def index(request):
    cars = Car.objects.all()
    models = ModelOfCar.objects.all()
    citys=City.objects.all()

    return render(request,'ourApp/index2.html',{'cars':cars,'models':models, 'citys':citys})

def about(request):
    contacts = Contact.objects.all()[:5]
    return render(request,'ourApp/about.html', {'contacts':contacts})


def get_by_id(request, car_id):
    return HttpResponse(Car.objects.get(id=car_id))

def services(request):
    contacts = Contact.objects.all()[:5]
    return render(request,'ourApp/services.html', {'contacts':contacts})

def cars(request):
    cars=Car.objects.all()
    paginator=Paginator(cars,4)
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

def send_confirm_for_contact(email, full_name, subject):
    message = 'Dear, ' + full_name + '. We received your contact message about ' + subject + ' .'
    recepient = email
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)

def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            email = contact_form.cleaned_data.get('email_address')
            full_name = contact_form.cleaned_data.get('full_name')
            subject = contact_form.cleaned_data.get('subject')
            send_confirm_for_contact(email, full_name, subject)
            return redirect('index')
    else:
        contact_form = ContactForm()
    return render(request,'ourApp/contact.html', {'contact_form':contact_form})

def login(request):
    return render(request,'ourApp/login.html')

def send_confirm_for_register(email, name, surname, subject):
    message = 'Dear, ' + name + ' ' + surname + '. We are pleased to inform you that you successfully created a new account .' + 'Sincerely yours. NomadRent'
    recepient = email
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            surname = form.cleaned_data.get('surname')
            subject = 'Registration'
            send_confirm_for_register(email, name, surname, subject)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request,'ourApp/register.html', {'form': form})

@login_required
def user_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'ourApp/user_update.html', {'user_form':form})

@login_required
def profile(request):
    return render(request, 'ourApp/profile.html')

def order(request):
    cars=Car.objects.all()
    models = ModelOfCar.objects.all()
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
            if request.POST['pickdate']:
                cars_location=Car.objects.filter(Q(city_id=City.objects.get(name__icontains=location),start_date__gte=convert(returndate))|Q(city_id=City.objects.get(name__icontains=location),end_date__lte=convert(pickdate))|Q(city_id=City.objects.get(name__icontains=location),available=True))

                print(convert(returndate))
            elif request.POST['pickdate']:
                cars_location=Car.objects.filter(city_id=City.objects.get(name__icontains=location),end_date__lte=convert(pickdate))

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
                'order':order,
                'models':models
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

def parse(date):
    list_of_date = date.split('/')
    return list_of_date

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False

def send_confirm_for_order(email, full_name, subject):
    message = 'Dear, ' + full_name + '. We are pleased to inform you that your order successfully confirmed. To see your order you can register by followed email (' + email + ') and go to profile page to show it. Sincerely yours. NomadRent'
    recepient = email
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)

def confirmation(request):
    location=''
    car_id=''
    pickdate=''
    returndate=''
    email_address=''
    if request.method == 'POST':
        location=request.POST.get('location')
        car_id = request.POST.get('car_id')
        pickdate=request.POST.get('pickdate')
        returndate = request.POST.get('returndate')
        print(location)
        print(car_id)
        print(pickdate)
        print(returndate)
        if validateEmail(request.POST.get('email')):
            email_address = request.POST.get('email')
            c = get_object_or_404(Car, pk=car_id)
            pick_list = parse(pickdate)
            return_list = parse(returndate)
            print(pick_list)
            pick_date_finally = date(int(pick_list[2]), int(pick_list[0]), int(pick_list[1]))
            return_date_finally = date(int(return_list[2]), int(return_list[0]), int(return_list[1]))
            difference_date = return_date_finally - pick_date_finally
            total_price = difference_date.days*c.price_hourly
            c.start_date = pick_date_finally
            c.end_date = return_date_finally
            c.save()
            if request.user.is_authenticated:
                if request.user.bank_card_id.pk == 1 and request.user.license_id.pk == 1:
                    bank_card_form = BankCardForm(request.POST)
                    driver_license_form = DriverLicenseForm(request.POST, request.FILES)
                else:
                    bank_card_form = BankCardForm(request.POST, instance=request.user.bank_card_id)
                    driver_license_form = DriverLicenseForm(request.POST, request.FILES, instance=request.user.license_id)
            else:
                bank_card_form = BankCardForm(request.POST)
                driver_license_form = DriverLicenseForm(request.POST, request.FILES)

            if bank_card_form.is_valid() and driver_license_form.is_valid():
                order = Order()
                order.car_id = c
                order.total_price = total_price
                order.email_address = email_address
                order.total_price = total_price
                order.start_date = pick_date_finally
                order.end_date = return_date_finally
                if request.user.is_authenticated:
                    order.user_id = SimpleUser.objects.get(pk=request.user.pk)
                    if request.user.bank_card_id.pk == 1 and request.user.license_id.pk == 1:
                        print('request.user.pk')
                        order.bank_card_id = request.user.bank_card_id = bank_card_form.save()
                        order.license_id = request.user.license_id = driver_license_form.save()
                        request.user.save()
                    else:
                        order.bank_card_id = bank_card_form.save()
                        order.license_id = driver_license_form.save()
                else:
                    order.bank_card_id = bank_card_form.save()
                    order.license_id = driver_license_form.save()
                    try:
                        user = SimpleUser.objects.get(email=email_address)
                    except:
                        send_confirm_for_order(email_address, order.bank_card_id.full_name, 'Order has confirmed')
                order.save()
                return redirect('index')


    if request.user.is_authenticated :
        if request.user.bank_card_id.pk == 1 and request.user.license_id.pk == 1:
            bank_card_form = BankCardForm()
            driver_license_form = DriverLicenseForm()
        else:
            bank_card_form = BankCardForm(instance=request.user.bank_card_id)
            driver_license_form = DriverLicenseForm(instance=request.user.license_id)
    else:
        bank_card_form = BankCardForm()
        driver_license_form = DriverLicenseForm()

    context = {
        'bank_card_form':bank_card_form,
        'driver_license_form':driver_license_form,
        'location':location,
        'car_id':car_id,
        'pickdate':pickdate,
        'returndate':returndate
    }
    return render(request,'ourApp/confirmation.html', context)


def car_info(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'ourApp/car_info.html', {'car':car})

def user_orders(request):
    print(request.user.email)
    user_orders_actual = Order.objects.all().filter(email_address=request.user.email, finished=False, canceled=False)
    user_orders_history = Order.objects.all().filter(Q(email_address=request.user.email)&(Q(finished=True)|Q(canceled=True)))
    return render(request, 'ourApp/user_orders.html', {'user_orders_actual':user_orders_actual, 'user_orders_history':user_orders_history})
