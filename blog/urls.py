from django.urls import path
from . import views
urlpatterns = [
    path('', views.evaluacion2, name=' evaluacion2'),
]
