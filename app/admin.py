from django.contrib import admin

# Register your models here.
from .models import Category, Product, Sub_Category, Contact_us, Order, Brand

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product)
admin.site.register(Contact_us)
admin.site.register(Order)
admin.site.register(Brand)