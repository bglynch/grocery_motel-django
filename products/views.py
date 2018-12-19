from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import BaseProduct


def get_products(request):
    products = BaseProduct.objects.all()

    return render(request, "products/index.html", {'products': products})
