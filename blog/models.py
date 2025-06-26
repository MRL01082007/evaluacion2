from django.conf import settings
from django.db import models
from django.utils import timezone

class Juegos_Indie(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    Nombre_del_juego_indie = models.TextField()
    Fecha_de_salida = models.DateTimeField(blank=True, null=True)
    Descripcion = models.TextField()
    Precio = models.TextField()
    Plataformas_disponibles = models.TextField()
    Fecha_de_la_ultima_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    hora_creacion = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
