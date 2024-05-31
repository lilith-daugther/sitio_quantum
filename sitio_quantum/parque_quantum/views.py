from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from .models import Actividades

#Función para el envío de correos desde la página
def enviar_correo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '') #parámetros requeridos
        email = request.POST.get('email', '')
        mensaje = request.POST.get('mensaje', '')

        # Configura los detalles del correo electrónico
        correo_destino = 'ambientalquantum2020@gmail.com' #falta llave pública, revisar.
        asunto_correo = f'Mensaje de {nombre}'
        cuerpo_correo = f'Nombre: {nombre}\nCorreo electrónico: {email}\n\nMensaje:\n{mensaje}'

        # Envía el correo electrónico
        send_mail(asunto_correo, cuerpo_correo, email, [correo_destino])

    return render(request, 'inicio.html')

#Redireccionamientos simples a las templates
def inicio(request):
    return render(request, "inicio.html")

def areas(request):
    return render(request,"areas.html")


def base2(request):
    return render(request,"base2.html")

def colecciones(request):
    return render(request, "colecciones.html")


def biodiversidad(request):
    return render(request, "biodiversidad.html")

def actividades(request):
    return render(request, "actividades.html")

def proyeccion(request):
    return render(request, "proyeccion.html")

def lista_actividades(request):
    actividades = Actividades.objects.all().order_by('-fecha')
    return render(request, 'actividades.html', {'actividades': actividades})