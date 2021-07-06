from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1 style='color:red;'>Hola <b>Mundo!</b></h1>")

def harry(request):
    return HttpResponse("¡Hola Harry!")

def hermione(request):
    return HttpResponse("¡Hola Hermione!")

def hola(request, nombre: str):
    return HttpResponse(f"¡Hola, {nombre.capitalize()}, es un gusto!")

def plantilla(request):
    return render(request, "hola/index.html")

def saludar(request, nombre_parametro:str):
    return render(request, "hola/saludar.html", {
        "nombre": nombre_parametro.capitalize()
    })