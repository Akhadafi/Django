from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the accounts home.")


def products(request):
    return HttpResponse("Hello, world. You're at the accounts products.")


def customer(request):
    return HttpResponse("Hello, world. You're at the accounts customer.")
