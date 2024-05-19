from django.db import models

class MiModelo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return self.nombre
