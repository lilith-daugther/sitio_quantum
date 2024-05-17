from django.db import models

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes_actividades/')  # Asegúrate de configurar MEDIA_ROOT y MEDIA_URL
    fecha = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
    
