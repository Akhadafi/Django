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


class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "customer",
        "product",
        "note",
        "date_created",
        "status",
    ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Tag, TagAdmin)
