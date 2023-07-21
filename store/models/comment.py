from .customer import Customer
from .product import Products
from django.db import models

class Comment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.customer)