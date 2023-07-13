from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Products
from store.models.orders import Order
from datetime import datetime
from django.utils import timezone
import json

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        username = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(timezone.now())

        order = Order(products= [],
                      customer=Customer(username=username),
                      address=address,
                      phone=phone,
                      date=datetime.now(),
                      sum_price=0)

        for product in products:
            print(cart.get(str(product.id)))

            total_price = product.price * int(cart.get(str(product.id)))
            order.products.append((product.image.url, product.name, product.price,
                                   int(cart.get(str(product.id))), total_price))
        for product in order.products:
            order.sum_price += int(product[4])
        order.save()
        request.session['cart'] = {}

        return redirect('cart')
