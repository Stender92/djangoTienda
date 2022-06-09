from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='ID Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre Categoria')

    def __str__(self):
        return (self.nombreCategoria)



class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='ID Producto')
    nombreProducto = models.CharField(max_length=100, verbose_name='Nombre Producto')
    precio = models.IntegerField(verbose_name='Precio Producto')
    stock = models.IntegerField(verbose_name="Stock Producto")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return (self.nombreProducto)

class Foto(models.Model):
    idFoto = models.IntegerField(primary_key=True)
    nombreFoto = models.CharField(max_length=100)
    nombreArchivo = models.CharField(max_length=256)
    descripcion = models.CharField(max_length=500)
    fechaPublicacion = models.DateField

    def __str__(self):
        return self.nombreFoto
