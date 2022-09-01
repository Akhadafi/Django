from django.shortcuts import render, redirect
from accounts.models import *
from accounts.forms import OrderForm
from django.forms import inlineformset_factory
from accounts.filters import OrderFilter


def index(request):
    memesan = Order.objects.all()
    pelanggan = Customer.objects.all()
    total_pelanggan = pelanggan.count()
    total_memesan = memesan.count()
    terkirim = memesan.filter(status="Terkirim").count()
    tertunda = memesan.filter(status="Tertunda").count()
    context = {
        "pelanggan": pelanggan,
        "memesan": memesan,
        "total_memesan": total_memesan,
        "total_pelanggan": total_pelanggan,
        "terkirim": terkirim,
        "tertunda": tertunda,
    }
    return render(request, "accounts/dashboard.html", context)


def produk(request):
    produk = Product.objects.all()
    context = {
        "produk": produk,
    }
    return render(request, "accounts/produk.html", context)


def pelanggan(request, pk):
    pelanggan = Customer.objects.get(id=pk)
    memesan = pelanggan.order_set.all()
    total_produk = memesan.count()
    myFilter = OrderFilter(request.GET, queryset=memesan)
    memesan = myFilter.qs
    context = {
        "pelanggan": pelanggan,
        "memesan": memesan,
        "total_produk": total_produk,
        "myFilter": myFilter,
    }
    return render(request, "accounts/pelanggan.html", context)


def tambah_pemesan(request, pk):
    OrderFormSet = inlineformset_factory(
        Customer, Order, fields=("produk", "status"), extra=8
    )
    pelanggan = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=pelanggan)
    # form = OrderForm(initial={"pelanggan": pelanggan})
    if request.method == "POST":
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=pelanggan)
        if formset.is_valid():
            formset.save()
            return redirect("dashboard")
    context = {"formset": formset}
    return render(request, "accounts/form_memesan.html", context)


def perbarui_pemesan(request, pk):
    memesan = Order.objects.get(id=pk)
    form = OrderForm(instance=memesan)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=memesan)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {"form": form}
    return render(request, "accounts/form_memesan.html", context)


def hapus_pemesan(request, pk):
    memesan = Order.objects.get(id=pk)
    if request.method == "POST":
        memesan.delete()
        return redirect("dashboard")
    context = {"item": memesan}
    return render(request, "accounts/hapus.html", context)
