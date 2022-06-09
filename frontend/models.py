from django.db import models

# Create your models here.
# ------------------------------------------------------------------------------------------------------------------------------------- #
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='ID Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre Categoria')

    def __str__(self):
        return self.nombreCategoria
# ------------------------------------------------------------------------------------------------------------------------------------- #
class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='ID Producto')
    nombreProducto = models.CharField(max_length=100, verbose_name='Nombre Producto')
    nombreArchivo = models.CharField(max_length=256, verbose_name='Nombre Archivo')
    precioProducto = models.IntegerField(verbose_name='Precio Producto')
    ratingProducto = models.FloatField(verbose_name='Rating Producto')
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreProducto
# ------------------------------------------------------------------------------------------------------------------------------------- #
class Foto(models.Model):
    idFoto = models.IntegerField(primary_key=True, verbose_name='ID Foto')
    nombreFoto = models.CharField(max_length=100, verbose_name='Nombre Foto')
    nombreArchivo = models.CharField(max_length=256, verbose_name='Nombre Archivo')
    descripcion = models.CharField(max_length=500, verbose_name='Descripcion')

    def __str__(self):
        return self.nombreFoto
# ------------------------------------------------------------------------------------------------------------------------------------- #

