from django import forms
from .models import Inscripcion, Contacto

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