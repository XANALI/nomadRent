# NomadRent
We are team `Zhalgas jmot` and our project `NomadRent`

## Content
- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [Team](#team)
- [Contacts](#contacts)

## Installation
- All the `code` required to get started

### Clone
- Clone this repo to your local machine using `https://github.com/XANALI/nomadRent.git`

## Features 
1. SEARCHING AVAILABLE CARS BY DATE.
2. SEND YOUR    WISHES VIA CONTACT
3. FILTERING BY VOLUME OF GASOLINE, BY PRICE AND BY MODEL
4. AFTER ALL THINGS YOU DO WE'LL SEND YOU MESSAGE TO YOUR GMAIL ADDRESS
5. YOU CAN SEE YOUR ORDERS IN THE PROFILE PAGE THERE IS A BUTTON THAT OPENS A WINDOW WITH USER ORDERS
6. IF YOU CLICK ON A CAR IN AN INDEX OR IN A CARS PAGE, A PAGE OPENS WITH INDIVIDUAL DESCRIPTIONS OF THE CAR

## PROJECT RELEVANCE
These are very active progressive people who value mobility, stebility, comfort. They prefer to spend their free time with friends, with their family and in search of new intersting city events, ready to travel around our vast country


## Installed App's
```
INSTALLED_APPS = [
    'ourApp',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
## Routing of files
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'login'

MEDIA_URL = '/shop/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'shop/media/')
```
## Routing of Site
In the main `carRental` directory `urls.py`:
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(template_name='ourApp/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='ourApp/logout.html'),name='logout'),
    path('', include("ourApp.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
**In the `ourApp` app `urls.py`**:
```
urlpatterns = [
    path("", views.index, name="index"),
    path('about/',views.about,name="about"),
    path('car_info/<int:car_id>/', views.car_info, name="car_info"),
    path('services/',views.services,name="services"),
    path('cars/',views.cars,name="cars-without-sidebar"),
    path('contact/',views.contact,name="contact"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('profile/',views.profile,name="profile"),
    path('order/',views.order,name="order"),
    path('confirmation/',views.confirmation,name="confirmation"),
    path('user_update/',views.user_update,name="user_update"),
    path('user_orders/',views.user_orders,name="user_orders"),
]
```

# Audience
Companies in need of transport on business trips in other cities, residents of the city in which there are branches of our company, tourists from different countries, successful specialists, experts, representatives of creative professions.

## Team

|**Ryskhan Alikhan**|**Sarsen Zhalgas**|**Ibraimov Alisher**|**Mauletkhan Zhalgas**|
| :---: |:---:| :---:| :---:|
[![Ryskhan Alikhan](https://github.com/XANALI/nomadRent/blob/master/media/user_avas/fdsfd.jpg?s=200)]()|[![Sarsen Zhalgas](ourApp/media/user_avas/team-mem-1.png?s=200)]()|[![Ibraimov Alisher](ourApp/media/user_avas/team-mem-3.png?s=200)]()|[![Mauletkhan Zhalgas](ourApp/media/user_avas/team-mem-2.png?s=200)]()||*Team leader, Interface designer*|*Web developer*|*System analisys*|

> All of us from `CSSE-1806k`

## Contacts
- Our E-mails:
- Ryskhan Alikhan <a href="https://vk.com/xanaaali">`VK`</a>
- Sarsen Zhalgas <a href="https://vk.com/zhsarsen">`VK`</a>
- Ibraimov Alisher <a href="https://vk.com/aaaaaali">`VK`</a> 
- Mauletkhan Zhalgas <a href="https://vk.com/id445005727">`VK`</a>
- Write to us if you have question 
