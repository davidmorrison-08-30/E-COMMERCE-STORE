from store.models.product import Products
from django.shortcuts import render , redirect , HttpResponseRedirect

def search_feature(request):
    # Check if the request is a post request.
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['search_query']
        # Filter your model by the search query
        products = Products.objects.filter(name__contains=search_query)
        return render(request, 'index.html', {'query':search_query, 'products': products})
    return render(request, 'index.html',{})
