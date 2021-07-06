from django.urls import path
from . import views

app_name = "AEROLINEA"

urlpatterns = [
    path('', views.index, name='index'),
]
