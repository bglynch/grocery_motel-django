from django.shortcuts import render
from django.http import HttpResponse
from .models import BaseProduct
from django.contrib import messages


def get_products(request):
    products = BaseProduct.objects.all()
    return render(request, "products/index.html", {'products': products})