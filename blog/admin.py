from django.contrib import admin
from .models import Juegos_Indie
from .forms import JuegosIndieForm

class JuegosIndieAdmin(admin.ModelAdmin):
    form = JuegosIndieForm
admin.site.register(Juegos_Indie, JuegosIndieAdmin)