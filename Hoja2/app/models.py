from django.db import models

# Create your models here.

class persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre