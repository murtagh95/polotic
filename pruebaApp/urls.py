from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('harry', views.harry, name='harry'),
    path('hermione', views.hermione, name='hermione'),
    path('plantilla', views.plantilla, name='plantilla'),
    path('saludar/<str:nombre>', views.hola, name='hola'),
    path('saludo/<str:nombre_parametro>', views.saludar, name='saludar'),
]
