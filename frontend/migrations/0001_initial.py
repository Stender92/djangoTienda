# Generated by Django 4.0.1 on 2022-05-31 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID Categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre Categoria')),
            ],
        ),
    ]
