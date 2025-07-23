from django import forms
from .models import Inscripcion, Contacto, Eventos

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['nombre', 'apellido', 'email', 'telefono', 'edad']
        
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'mensaje']
        widgets = {
            'mensaje': forms.Textarea(attrs={'rows': 4}),
        }

class EventosForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = ['nombre', 'descripcion', 'fecha', 'ubicacion', 'imagen']
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }