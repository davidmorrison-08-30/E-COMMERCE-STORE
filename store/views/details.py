from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.comment import Comment
from store.models.customer import Customer
from django.views import View
from django.shortcuts import render, get_object_or_404
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('customer', 'product', 'body')

class ProductView(View):

	def get(self, request, prodid):
		product = Products.objects.filter(id=prodid)
		comments = product[0].comments.filter(active=True)
		print(prodid)
		customer = request.session.get('customer')
		new_comment = None
		return render(request, "details.html", {"product": product[0],
		                                        "prodid": prodid,
		                                        'customer': customer,
		                                        'comments': comments,
		                                        'new_comment': new_comment})

	def post(self, request, prodid):
		if request.method == 'POST':
			comment_form = CommentForm(data=request.POST)
			product = Products.objects.filter(id=prodid)
			if comment_form.is_valid():
				# Create Comment object but don't save to database yet
				new_comment = comment_form.save(commit=False)
				# Assign the current post to the comment
				new_comment.product = product[0]
				new_comment.customer = request.session.get('customer')
				# Save the comment to the database
				new_comment.save()
		else:
			comment_form = CommentForm()
		return HttpResponseRedirect("")