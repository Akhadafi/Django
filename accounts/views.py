from django.shortcuts import redirect, render

from .forms import OrderForm
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
    context = {
        "customer": customer,
        "orders": orders,
        "order_count": order_count,
    }
    return render(request, "accounts/customer.html", context)


def createOrder(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "accounts/order_form.html", context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "accounts/order_form.html", context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect("/")
    context = {"item": order}
    return render(request, "accounts/delete.html", context)
