from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Necesitamos tener las tareas en sesiones

class FormAltaTarea(forms.Form):
    tarea = forms.CharField(label='Nueva Tarea')


def index(request):
    if 'tareas' not in request.session:
        request.session['tareas'] = []

    return render(request, "tareas/index.html", {
        'tareas': request.session['tareas']
    })


def agregar(request):
    if request.method == 'POST':
        form = FormAltaTarea(request.POST)
        if form.is_valid():
            tarea = form.cleaned_data['tarea']
            request.session['tareas'] += [tarea]
            return HttpResponseRedirect(reverse('TAREAS:index'))
        else:
            return HttpResponseRedirect(reverse('TAREAS:agregar'), {
                "formulario_alta_tareas": form
            })

    return render(request, 'tareas/agregar.html', {
        "formulario_alta_tareas": FormAltaTarea()
    })
