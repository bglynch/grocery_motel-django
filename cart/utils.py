from django.shortcuts import get_object_or_404
from products.models import BaseProduct
from decimal import Decimal

def get_cart_items_and_total(cart):
    cart_items = []
    cart_total=0
    items_total=0
    for p in cart:
        product = get_object_or_404(BaseProduct, pk = p)
        
        cart_item = {
            'product':product, 
            'quantity':cart[p],
            'total':Decimal(product.price*cart[p]),
        }
        
        cart_items.append(cart_item)
        cart_total += Decimal(product.price*cart[p])
        items_total += cart[p]
    
    return {'cart_items':cart_items, 'cart_total':cart_total, 'items_total':items_total}