from django.contrib import admin
from django.forms import DateInput
from django.db import models
from .models import Juegos_Indie

class Juegos_Indie(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {'widget': DateInput(attrs={'type': 'date'})},
    }
admin.site.register(Juegos_Indie)
