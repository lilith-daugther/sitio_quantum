"""
URL configuration for sitio_quantum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from parque_quantum import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('areas/', views.areas, name='areas'),
    path('base/', views.base2, name='base'),
    path('enviar_correo/', views.enviar_correo, name='enviar_correo'),
    path('colecciones/', views.colecciones, name="colecciones"),
    path('biodiversidad/', views.biodiversidad, name="biodiversidad"),
    path('actividades/', views.lista_actividades, name="actividades"),
    path('proyeccion/', views.proyeccion, name="proyeccion"),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
