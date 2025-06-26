from django.contrib import admin
from .models import Juegos_Indie
from .forms import JuegosIndieForm

@admin.register(Juegos_Indie)
class JuegosIndieAdmin(admin.ModelAdmin):
    form = JuegosIndieForm

