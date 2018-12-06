from django.urls import path
import products.views as view


urlpatterns = [
    path('', view.get_products, name='get_products'),
    ]
