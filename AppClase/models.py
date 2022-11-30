from django.db import models #Modelos: como manejo mi base de datos, Tablas de las bases de datos

# Create your models here.

class Persona (models.Model):
    nombre= models.CharField(max_length=30)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    telefono=models.IntegerField()
    
