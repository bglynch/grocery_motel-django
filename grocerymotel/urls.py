"""grocerymotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/

"""
from django.contrib import admin
from django.urls import path, include
from home.views import get_home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home, name="home"),
]
