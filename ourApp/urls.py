from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('about/',views.about,name="about"),
    path('<int:car_id>/', views.get_by_id, name="detail"),
]
