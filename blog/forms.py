from django import forms
from .models import Juegos_Indie

class JuegosIndieForm(forms.ModelForm):
    class Meta:
        model = Juegos_Indie
        fields = '__all__'
        widgets = {
            'Fecha_de_salida': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'Fecha_de_la_ultima_actualizacion': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Fecha_de_salida'].input_formats = ['%Y-%m-%d', '%Y/%m/%d']
        self.fields['Fecha_de_la_ultima_actualizacion'].input_formats = ['%Y-%m-%d', '%Y/%m/%d']