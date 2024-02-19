from django.contrib import admin
from .models import Order, OrderElement
# Register your models here.
admin.site.register(Order)
admin.site.register(OrderElement)