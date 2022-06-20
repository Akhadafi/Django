from multiprocessing import context

from django.http import HttpResponse
from django.shortcuts import render

from .models import *


# Create your views here.
def home(request):
    # Customer
    customers = Customer.objects.all()
    total_customers = customers.count()
    # Order
    orders = Order.objects.all()
    total_oreders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()

    context = {
        # Customer
        "customers": customers,
        "total_customers": total_customers,
        # Order
        "orders": orders,
        "total_oreders": total_oreders,
        "delivered": delivered,
        "pending": pending,
    }
    return render(request, "accounts/dashboard.html", context)


def products(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "accounts/products.html", context)


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {"customer": customer, "orders": orders, "order_count": order_count}
    return render(request, "accounts/customer.html", context)
