from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Perfil

from .forms import PerfilForm, Registro


class UserRegistrationView(CreateView):
    model = User
    template_name = 'usuarios/registro.html'
    form_class = Registro
    success_url = reverse_lazy('login')
    
class LoginUsuario(LoginView):
    template_name = 'usuarios/login.html'
    
    def get_success_url(self):
        return reverse_lazy('inicio')
    
class LogoutUsuario(LogoutView):
    next_page = reverse_lazy('inicio')
    
class PerfilUsuario(DetailView):
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

class EditarPerfilUsuario(FormView):
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