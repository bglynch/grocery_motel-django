from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from products.models import BaseProduct
from .utils import get_cart_items_and_total


def get_cart(request):
    cart =  request.session.get('cart', {})
    context= get_cart_items_and_total(cart)
    return render(request, "cart/viewcart.html", context)


def cart_add(request):
    # Get the product were adding
    id = request.POST.get('product_id')
    product = get_object_or_404(BaseProduct, pk=id)
    messages.success(request, f"{product.name} added to your cart")
    # Get the current cart
    cart = request.session.get('cart', {})
    print('')
    print(cart)
    print(type(cart))
    # {}
    # <class 'dict'>    
    
    print('')
    
    # Update the cart
    cart[id] = cart.get(id, 0) + 1
    print(cart[id])
    print(type(cart[id]))
    # 1
    # <class 'int'>
    print(cart)
    print(type(cart))
    # {'1': 1}
    # <class 'dict'>
    
    # Save the cart back to the session
    request.session['cart'] = cart
    
    # Redirect to somewhere
    return redirect('get_products')


def cart_remove(request):
    id = request.POST.get('product_id')
    product = get_object_or_404(BaseProduct, pk=id)
    cart = request.session.get('cart', {})
    if cart.get(id) > 1:
       cart[id] = cart.get(id, 0) + -1
    else:
        del cart[id]
    request.session['cart'] = cart
    return redirect('get_cart')
