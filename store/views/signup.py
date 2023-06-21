from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup (View):
    def get(self, request):
        return render (request, 'signup.html')

    def post(self, request):
        postData = request.POST
        name = postData.get ('name')
        username = postData.get('username')
        password = postData.get ('password')
        # validation
        value = {
            'name': name,
            'username': username,
            'password': password
        }
        error_message = None

        customer = Customer (name=name,
                             username=username,
                             password=password)
        error_message = self.validateCustomer (customer)

        if not error_message:
            print (name, username, password)
            customer.password = make_password (customer.password)
            customer.register ()
            return redirect ('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if len (customer.password) < 12:
            error_message = 'Password must be 12 char long'
        elif customer.isExists ():
            error_message = 'Username Already Registered..'
        # saving

        return error_message