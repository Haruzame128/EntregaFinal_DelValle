from django.shortcuts import render
from django.views.generic import CreateView, DetailView, FormView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Instructor, Perfil

from .forms import InstructorForm, PerfilForm, Registro


class UserRegistrationView(CreateView):
    model = User
    template_name = 'usuarios/registro.html'
    form_class = Registro
    success_url = reverse_lazy('login')
    
class LoginUsuario(LoginView):
    template_name = 'usuarios/login.html'
    
    def get_success_url(self):
        return reverse_lazy('inicio')
    
class LogoutUsuario(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('inicio')
    
class PerfilUsuario(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'usuarios/perfil.html'
    context_object_name = 'usuario'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user

        # Crear perfil si no existe
        perfil, created = Perfil.objects.get_or_create(user=usuario)
        context['perfil'] = perfil
        return context

class EditarPerfilUsuario(LoginRequiredMixin, FormView):
    template_name = 'usuarios/editar_perfil.html'
    form_class = PerfilForm
    success_url = reverse_lazy('perfil')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'instance': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListaInstructores(ListView):
    model = Instructor
    template_name = 'usuarios/instructores.html'
    context_object_name = 'instructores'

    def get_queryset(self):
        return Instructor.objects.filter(activo=True)
    
class AgregarInstructorView(LoginRequiredMixin, CreateView):
    model = Instructor
    form_class = InstructorForm
    template_name = 'usuarios/agregar_instructor.html'
    success_url = reverse_lazy('instructores')

class InstructorDetailView(DetailView):
    model = Instructor
    template_name = 'usuarios/detalle_instructor.html'
    context_object_name = 'instructor'