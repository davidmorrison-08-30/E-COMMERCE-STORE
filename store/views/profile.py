from django.views import View
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.shortcuts import render , redirect , HttpResponseRedirect

class ProfileView(View):
	def get(self, request):
		customer = Customer.get_customer_by_username(request.session.get('customer'))
		return render(request, 'profile.html', {'customer': customer})

	def post(self, request):
		postData = request.POST
		name = postData.get('name')
		username = postData.get('username')
		# validation
		value = {
			'name': name,
			'username': username,
		}
		error_message = None

		customer.name = name, customer.username = username
		error_message = self.validateCustomer(customer)

		if not error_message:
			print(name, username)
			return redirect('profile')
		else:
			data = {
				'error': error_message,
				'values': value
			}
			return render(request, 'profile.html', data)

	def validateCustomer(self, customer):
		error_message = None
		if customer.isExists():
			error_message = 'Username Already Registered..'
		# saving

		return error_message