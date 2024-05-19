from django.contrib import admin
from .models import Actividades

@admin.register(Actividades)
class ActividadesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha')  # Campos que deseas mostrar en la lista del administrador
    search_fields = ('nombre', 'descripcion')  # Campos por los que puedes buscar
    ordering = ('-fecha',)  # Orden de las actividades
    fields = ['nombre', 'descripcion', 'fecha', 'imagen']  # Campos que se muestran en el formulario de creación/edición
