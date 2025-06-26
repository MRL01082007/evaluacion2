from django.contrib import admin
from django.db import models
from django.forms import DateInput
from .models import Juegos_Indie

class JuegosIndieAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {
            'widget': DateInput(
                attrs={
                    'type': 'date',
                    'lang': 'es',
                },
                format='%Y-%m-%d',  
            )
        }
    }

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        for field_name in ['Fecha_de_salida', 'Fecha_de_la_ultima_actualizacion']:
            if field_name in form.base_fields:
                form.base_fields[field_name].input_formats = ['%Y-%m-%d']
        return form

admin.site.register(Juegos_Indie, JuegosIndieAdmin)