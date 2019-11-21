from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('about/',views.about,name="about"),
    path('<int:car_id>/', views.get_by_id, name="detail"),
    path('services/',views.services,name="services"),
    path('cars/',views.cars,name="cars-without-sidebar"),
    path('contact/',views.contact,name="contact"),
]
