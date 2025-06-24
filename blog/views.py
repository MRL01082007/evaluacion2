from django.shortcuts import render
from django.utils import timezone
from .models import Juegos_Indie

def evalua2(request):
    publicaciones=Juegos_Indie.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/evalua2.html',{'publicaciones':publicaciones})
