from django.shortcuts import render
from .models import Persona
from django.http import HttpResponse

# Create your views here.

def Padre (request):
    padre= Persona(nombre="Gabriel", apellido="olivo", edad=51, telefono=2222222222)
    padre.save()
    cadena_texto=f"Familiar Guardado: Nombre={padre.nombre}, Apellido={padre.apellido}, edad={padre.edad}, telefono={padre.telefono}"
    return HttpResponse(cadena_texto)

def Madre (request):
    madre= Persona(nombre="Susana", apellido="Disca", edad=51, telefono=3333333333)
    madre.save()
    cadena_texto=f"Familiar Guardado: Nombre={madre.nombre}, Apellido={madre.apellido}, edad={madre.edad}, telefono={madre.telefono}"
    return HttpResponse(cadena_texto)

def Hermano (request):
    hermano= Persona(nombre="Agustin", apellido="Terreno", edad=29, telefono=2222222222)
    hermano.save()
    cadena_texto=f"Familiar Guardado: Nombre={hermano.nombre}, Apellido={hermano.apellido}, edad={hermano.edad}, telefono={hermano.telefono}"
    return HttpResponse(cadena_texto)