from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.EmailField(primary_key=True)
    nombre = models.CharField(max_length=100)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
