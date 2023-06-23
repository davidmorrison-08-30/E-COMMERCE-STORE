from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Products
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        username = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(address, phone, username, cart, products)

        order = Order(customer=Customer(username=username),
                      address=address,
                      phone=phone)
        order.save()
        total_price = total_quantity = 0
        for product in products:
            print(cart.get(str(product.id)))
            order.products.add(product)
            total_price += product.price
            total_quantity += cart.get(str(product.id))
        order.price = total_price
        order.quantity = total_quantity
        request.session['cart'] = {}

        return redirect('cart')
