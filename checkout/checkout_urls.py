from django.urls import path
import checkout.views as view


urlpatterns = [
    path('', view.go_to_checkout, name='go_to_checkout'),
    ]
