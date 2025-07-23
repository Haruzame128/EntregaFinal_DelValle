from django.shortcuts import render
from .forms import InscripcionForm, ContactoForm, EventosForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView, DetailView, ListView
from django.urls import reverse_lazy
from .models import Inscripcion, Eventos
from django.contrib.auth.mixins import LoginRequiredMixin

class InscripcionDeleteView(LoginRequiredMixin, DeleteView):
    model = Inscripcion
    success_url = reverse_lazy('lista_inscriptos') 
    template_name = 'confirmar_eliminacion.html'
    
class DetalleEventoView(DetailView):
    model = Eventos
    template_name = 'HashiDojo/detalle_evento.html'
    context_object_name = 'evento'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['evento'] = self.get_object()
        return context
    
class ListaEventosView(ListView):
    model = Eventos
    template_name = 'HashiDojo/lista_eventos.html'
    context_object_name = 'eventos'

    def get_queryset(self):
        return Eventos.objects.all()
    
class EventoDeleteView(LoginRequiredMixin, DeleteView):
    model = Eventos
    template_name = 'confirmar_eliminacion_evento.html'
    success_url = reverse_lazy('lista_eventos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['evento'] = self.get_object()
        return context

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
            return render(request, 'HashiDojo/inscripcion_exitosa.html')  
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

def acceso_denegado(request):
    return render(request, 'HashiDojo/acceso_denegado.html')

@login_required
def crear_eventos(request):
    if request.method == 'POST':
        form = EventosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'HashiDojo/evento_creado.html')
    else:
        form = EventosForm()
    return render(request, 'HashiDojo/cargar_eventos.html', {'form': form})