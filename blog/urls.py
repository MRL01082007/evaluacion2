from django.urls import path
from . import views
urlpatterns = [
    path('evaluacion2/', views.evaluacion2, name='evaluacion2'),
]
