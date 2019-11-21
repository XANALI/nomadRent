
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(template_name='ourApp/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='ourApp/templates/ourApp/logout.html'),name='logout'),
    path('', include("ourApp.urls")),
]
