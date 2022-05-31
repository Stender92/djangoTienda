from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='ID Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre Categoria')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='ID Producto')
    nombreProducto = models.CharField(max_length=100, verbose_name='Nombre Producto')
    precioProducto = models.IntegerField(verbose_name='Precio Producto')
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre