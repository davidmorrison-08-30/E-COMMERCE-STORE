from django.views import View
from store.models.customer import Customer
from django.shortcuts import render , redirect , HttpResponseRedirect

class ProfileView(View):
	def get(self, request):
		customer = request.session.get('customer')
		return render(request, 'profile.html', {'customer': customer})