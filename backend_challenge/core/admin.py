from django.contrib import admin

from .models import Customer, Order

admin.site.register(Customer)
admin.site.register(Order)

# Register your models here.
