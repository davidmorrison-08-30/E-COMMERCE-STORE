from django.views import View
from django.views.generic import  ListView
from store.models.customer import Customer
from store.models.product import Products
from django.shortcuts import render , redirect , HttpResponseRedirect

class SearchView(View):
	model = Products
	template_name = "search.html"
	context_object_name = "posts"

	def get_queryset(self):
		query = self.request.GET.get("q")
		return Products.objects.filter(name__contains=query)
