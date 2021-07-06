from django.shortcuts import render
from .models import Vuelo


def index(request):
    return render(request, 'vuelos/index.html', {
        'lista_vuelos': Vuelo.objects.all()
    })

