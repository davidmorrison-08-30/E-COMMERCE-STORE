from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from django.views import View

class ProductView(View):

	def get(self, request, prodid):
		product = Products.objects.filter(id=prodid)
		print(product[0].name)
		return render(request, "details.html", {"product": product[0]})