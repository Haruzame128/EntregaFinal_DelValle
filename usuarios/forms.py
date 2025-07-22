from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class Registro(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(Registro, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class PerfilForm(forms.ModelForm):
    telefono = forms.CharField(required=False)
    direccion = forms.CharField(required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        user = kwargs.get('instance')
        super().__init__(*args, **kwargs)

        if hasattr(user, 'perfil'):
            self.fields['telefono'].initial = user.perfil.telefono # type: ignore
            self.fields['direccion'].initial = user.perfil.direccion # type: ignore
            self.fields['avatar'].initial = user.perfil.avatar # type: ignore

    def save(self, commit=True):
        user = super().save(commit)
        perfil = user.perfil
        perfil.telefono = self.cleaned_data['telefono']
        perfil.direccion = self.cleaned_data['direccion']
        if self.cleaned_data['avatar']:
            perfil.avatar = self.cleaned_data['avatar']
        perfil.save()
        return user


