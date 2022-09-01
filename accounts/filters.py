import django_filters
from accounts.models import *
from django_filters import DateFilter, CharFilter


class OrderFilter(django_filters.FilterSet):
    tanggal_mulai = DateFilter(field_name="tanggaldibuat", lookup_expr="gte")
    tanggal_akhir = DateFilter(field_name="tanggaldibuat", lookup_expr="lte")
    catatan = CharFilter(field_name="note", lookup_expr="icontains")

    class Meta:
        model = Order
        fields = "__all__"
        exclude = ["pelanggan", "tanggaldibuat"]
