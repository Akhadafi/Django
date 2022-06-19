from django.contrib import admin

from .models import *


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "phone",
        "email",
        "date_created",
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "category",
        "description",
        "date_created",
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "date_created",
        "status",
    ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
