"""grocerymotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/

"""
from django.contrib import admin
from django.urls import path, include
from checkout import checkout_urls
from cart import cart_urls
from products import products_urls
from home.views import get_home
from accounts import accounts_urls
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkout/', include(checkout_urls)),
    path('cart/', include(cart_urls)),
    path('products/', include(products_urls)),
    path('auth/', include('social_django.urls', namespace='social')),
    path('', include(accounts_urls)),
    path('', get_home, name="home"),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
