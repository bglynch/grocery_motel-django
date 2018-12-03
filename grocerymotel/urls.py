"""grocerymotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/

"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from home.views import get_home
from accounts import views as accounts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_account/', accounts_views.my_account, name='my_account'),
    path('register/', accounts_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),    
    path('', get_home, name="home"),
]
