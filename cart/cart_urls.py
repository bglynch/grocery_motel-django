from django.urls import path
import cart.views as view


urlpatterns = [
    path('', view.get_cart, name='get_cart'),
    path('add', view.cart_add, name='cart_add'),
    path('remove', view.cart_remove, name='cart_remove'),
    ]
