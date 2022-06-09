# Generated by Django 4.0.1 on 2022-05-31 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID Producto')),
                ('nombreProducto', models.CharField(max_length=100, verbose_name='Nombre Producto')),
                ('precioProducto', models.IntegerField(verbose_name='Precio Producto')),
                ('stockProducto', models.IntegerField(verbose_name='Stock Producto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.categoria', verbose_name='Categoria')),
            ],
        ),
    ]
