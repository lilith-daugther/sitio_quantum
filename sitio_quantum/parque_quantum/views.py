from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Actividades
from .admin import ActividadesAdmin


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

def CRUDactividades(request):
    return render(request, "CRUD_actividades.html")


# CRUD de actividades
class ActividadesListView(ListView):
    model = Actividades
    context_object_name = 'objetos'

class ActividadesCreateView(CreateView):
    model = Actividades
    form_class = ActividadesAdmin
    success_url = reverse_lazy('lista')
    template_name = 'actividades_form.html'

class ActividadesUpdateView(UpdateView):
    model = Actividades
    form_class = ActividadesAdmin
    success_url = reverse_lazy('lista')

class ActividadesDeleteView(DeleteView):
    model = Actividades
    success_url = reverse_lazy('lista')
    template_name = 'mi_app/Actividades_confirm_delete.html'

def lista_actividades(request):
    actividades = Actividades.objects.all().order_by('-fecha')
    return render(request, 'templates/actividades.html', {'actividades': actividades})