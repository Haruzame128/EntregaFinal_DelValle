from django.shortcuts import render
from .forms import InscripcionForm, ContactoForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def inicio(request):
    return render(request, 'HashiDojo/inicio.html')

def acercaDeMi(request):
    return render(request, 'HashiDojo/acerca_de_mi.html')

def clases(request):
    return render(request, 'HashiDojo/clases.html')

def inscripcion(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'HashiDojo/inscripcion_exitosa.html')  # página de agradecimiento
    else:
        form = InscripcionForm()
    return render(request, 'HashiDojo/inscripcion.html', {'form': form})

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Guardamos el mensaje en la base de datos
            form.save()
            return render(request, 'HashiDojo/contacto_exitosa.html')  # Página de confirmación
    else:
        form = ContactoForm()

    return render(request, 'HashiDojo/contacto.html', {'form': form})