from django import forms

from .models import consulta


class PostForm(forms.ModelForm):
    
    class Meta:
        model = consulta
        fields = ('Rut', 'Nombres','Correo','Telefono','Asunto')
    