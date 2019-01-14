from django.db import models
from django.contrib.auth.models import User
from products.models import BaseProduct


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address_1 = models.CharField(max_length=40, blank=False)
    street_address_2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, related_name="line_items", on_delete=models.CASCADE)
    product = models.ForeignKey(BaseProduct, null=False, related_name="orders", on_delete=models.PROTECT)
    quantity = models.IntegerField(blank=False)
    shopper = models.ForeignKey(User, null=False, related_name="orders_shopper", on_delete=models.PROTECT)

    def __str__(self):
        return f"ShopperID:{self.shopper.id}: {self.quantity}No. {self.product.name} @ {self.product.price}--Order{self.order.id}"