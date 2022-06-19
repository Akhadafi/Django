from django import views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("products", views.products, name="products"),
    path("customer/", views.customer, name="customer"),
]
