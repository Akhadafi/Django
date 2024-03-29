# Generated by Django 3.2.15 on 2022-08-31 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20220830_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('harga', models.PositiveIntegerField(null=True)),
                ('kategori', models.CharField(choices=[('dalam ruangan', 'dalam ruangan'), ('luar ruangan', 'luar ruangan')], max_length=200, null=True)),
                ('deskripsi', models.CharField(blank=True, max_length=200, null=True)),
                ('tanggaldibuat', models.DateTimeField(auto_now_add=True, null=True)),
                ('tags', models.ManyToManyField(to='accounts.Tag')),
            ],
        ),
        migrations.RenameModel(
            old_name='Pelanggan',
            new_name='Customer',
        ),
        migrations.RenameModel(
            old_name='Memesan',
            new_name='Order',
        ),
        migrations.DeleteModel(
            name='Produk',
        ),
        migrations.AlterField(
            model_name='order',
            name='produk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.product'),
        ),
    ]
