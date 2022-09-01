from django.db import models

# Create your models here.
class Customer(models.Model):
    nama = models.CharField(max_length=200, null=True)
    no_hp = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    tanggaldibuat = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama


class Tag(models.Model):
    nama = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nama


class Product(models.Model):
    KATEGORI = (
        ("dalam ruangan", "dalam ruangan"),
        ("luar ruangan", "luar ruangan"),
    )
    nama = models.CharField(max_length=200, null=True)
    harga = models.PositiveIntegerField(null=True)
    kategori = models.CharField(max_length=200, null=True, choices=KATEGORI)
    deskripsi = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    tanggaldibuat = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama


class Order(models.Model):
    STATUS = (
        ("Tertunda", "Tertunda"),
        ("Keluar untuk pengiriman", "Keluar untuk pengiriman"),
        ("Terkirim", "Terkirim"),
    )
    pelanggan = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    produk = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    tanggaldibuat = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return f"{self.produk.nama} - {self.status}"
