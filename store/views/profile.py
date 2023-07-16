from django.views import View
from store.models.customer import Customer
from store.models.orders import Order
from django.contrib.auth.hashers import make_password
from django.shortcuts import render , redirect , HttpResponseRedirect

class ProfileView(View):
	def get(self, request):
		customer = Customer.get_customer_by_username(request.session.get('customer'))
		num_orders = Order.objects.filter(customer=customer.username).count()
		print(num_orders)
		return render(request, 'profile.html', {'customer': customer, "num_orders": num_orders})