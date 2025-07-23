from django.shortcuts import render
from .forms import InscripcionForm, ContactoForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Inscripcion
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def inicio(request):
    return render(request, 'HashiDojo/inicio.html')

def acercaDeMi(request):
    return render(request, 'HashiDojo/about.html')

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

@login_required
def lista_inscriptos(request):
    inscriptos = Inscripcion.objects.all()
    return render(request, 'HashiDojo/listaInscriptos.html', {'inscriptos': inscriptos})
    
class InscripcionDeleteView(LoginRequiredMixin, DeleteView):
    model = Inscripcion
    success_url = reverse_lazy('lista_inscriptos') 
    template_name = 'confirmar_eliminacion.html'

def acceso_denegado(request):
    return render(request, 'HashiDojo/acceso_denegado.html')