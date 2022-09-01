from django.urls import path
from accounts import views

urlpatterns = [
    path("", views.index, name="dashboard"),
    path("produk/", views.produk, name="produk"),
    path("pelanggan/<str:pk>/", views.pelanggan, name="pelanggan"),
    path("tambah_pemesan/<str:pk>/", views.tambah_pemesan, name="tambah_pemesan"),
    path("perbarui_pemesan/<str:pk>/", views.perbarui_pemesan, name="perbarui_pemesan"),
    path("hapus_pemesan/<str:pk>/", views.hapus_pemesan, name="hapus_pemesan"),
]
