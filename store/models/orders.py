from django.db import models
from .product import Products
from .customer import Customer
# from django.contrib.postgres.fields import JSONField
from datetime import datetime


class Order(models.Model):
    products = models.JSONField()
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=10, default='', blank=True)
    date = models.DateField(default=datetime.now)
    sum_price = models.IntegerField()
    status = models.BooleanField(default=False) # False ~ Pending, True ~ Delivered

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

