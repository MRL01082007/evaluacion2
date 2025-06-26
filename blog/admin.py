from django.contrib import admin
from .models import Juegos_Indie
from .forms import JuegosIndieForm

class JuegosIndieAdmin(admin.ModelAdmin):
    form = JuegosIndieForm
    readonly_fields = ['fecha_publicacion', 'hora_creacion']
admin.site.register(Juegos_Indie, JuegosIndieAdmin)