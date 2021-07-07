from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Establesco los permisos
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .models import Vuelo, Pasajero


def index(request):
    return render(request, 'vuelos/index.html', {
        'lista_vuelos': Vuelo.objects.all()
    })

# Restringimos el acceso por el siguiente permiso
@permission_required('AEROLINEA.view_vuelo')
def vuelo(request, vuelo_id):
    # Busco el vuelo por id
    vuelo = Vuelo.objects.get(id=vuelo_id)
    # Busco todos los que no son pasajeros del vuelo
    no_son_pasajeros = Pasajero.objects.exclude(vuelos=vuelo).all()
    # Busco los pasajeros que estan registrados a dicho vuelo
    pasajeros = vuelo.pasajeros.all()
    return render(request, 'vuelos/vuelo.html', {
        "vuelo": vuelo,
        "pasajeros": pasajeros,
        "no_son_pasajeros": no_son_pasajeros,
    })

@login_required
def reserva(request, vuelo_id):
    if request.method == "POST": 
        vuelo = Vuelo.objects.get(pk=vuelo_id)

        pasajero_id = int(request.POST.get('pasajero'))

        pasajero = Pasajero.objects.get(pk=pasajero_id)  # Busca por primary key

        pasajero.vuelos.add(vuelo)  # Agrego el vuelo al pasajero

        return HttpResponseRedirect(reverse("AEROLINEA:vuelo", args=(vuelo_id,)))
