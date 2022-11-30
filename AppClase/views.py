from django.shortcuts import render
from .models import Persona
from django.http import HttpResponse

# Create your views here.

def Padre (request):
    padre= Persona(nombre="Gabriel", apellido="olivo", edad=51, telefono=2222222222)
    padre.save()
    cadena_texto=f"Familiar Guardado: Nombre={padre.nombre}, Apellido={padre.apellido}, edad={padre.edad}, telefono={padre.telefono}"
    return HttpResponse(cadena_texto)