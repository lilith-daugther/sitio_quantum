from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Actividad
from .forms import ActividadForm
from django.http import JsonResponse
from .models import Actividad
from django.views.decorators.csrf import csrf_exempt


def inicio(request):
    return render(request, "inicio.html")

def areas(request):
    return render(request,"areas.html")


def base2(request):
    return render(request,"base2.html")

def enviar_correo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        email = request.POST.get('email', '')
        mensaje = request.POST.get('mensaje', '')

        # Configura los detalles del correo electrónico
        correo_destino = 'kaithlyn.mendez@gmail.com'
        asunto_correo = f'Mensaje de {nombre}'
        cuerpo_correo = f'Nombre: {nombre}\nCorreo electrónico: {email}\n\nMensaje:\n{mensaje}'

        # Envía el correo electrónico
        send_mail(asunto_correo, cuerpo_correo, email, [correo_destino])

    return render(request, 'inicio.html')

def colecciones(request):
    return render(request, "colecciones.html")


def biodiversidad(request):
    return render(request, "biodiversidad.html")

def actividades(request):
    return render(request, "actividades.html")


class ActividadListView(ListView):
    model = Actividad
    context_object_name = 'actividades'

class ActividadCreateView(CreateView):
    model = Actividad
    form_class = ActividadForm
    success_url = reverse_lazy('actividades')

class ActividadUpdateView(UpdateView):
    model = Actividad
    form_class = ActividadForm
    success_url = reverse_lazy('actividades')

class ActividadDeleteView(DeleteView):
    model = Actividad
    success_url = reverse_lazy('actividades')


@csrf_exempt  # Solo para demostración; idealmente maneja la CSRF de otra forma
def crear_actividad(request):
    print('hola entrè')
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        fecha = request.POST.get('fecha')
        descripcion = request.POST.get('descripcion')
        actividad = Actividad.objects.create(nombre=nombre, fecha=fecha, descripcion=descripcion)
        return JsonResponse({'id': actividad.id})  # Retorna el id de la actividad creada o algún mensaje
    return JsonResponse({'error': 'Método no permitido'}, status=405)

