from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from django.utils.html import format_html
from django.utils.safestring import mark_safe

class AdminCustomer(admin.ModelAdmin):
    list_display = ['name', 'username', 'password']

class AdminOrder(admin.ModelAdmin):
    list_display = ['order', 'customer', 'address', 'phone', 'date', 'display_products', 'sum_price', 'status']
   # list_display_links = None  # Disable linking to the detail view

    # def display_order(self, obj):
    #     return format_html('<a href="%s"></a>' % (obj))
    #
    # display_order.short_description = 'References to YourModel'

    def display_products(self, obj):
        elements = obj.products
        return mark_safe("<br>".join(str(element[3])+"x "+str(element[1]+", "+str(element[2])) for element in elements))

    display_products.short_description = 'Products'

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)
