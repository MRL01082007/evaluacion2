from django import forms
from .models import Juegos_Indie

class JuegosIndieForm(forms.ModelForm):
    class Meta:
        model = Juegos_Indie
        fields = '__all__'
        widgets = {
            'Fecha_de_salida': forms.DateInput(attrs={'type': 'date'}),
            'Fecha_de_la_ultima_actualizacion': forms.DateInput(attrs={'type': 'date'}),
        }