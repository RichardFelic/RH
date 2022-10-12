from email.policy import default
from random import choices
from re import S
from secrets import choice
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# IDIOMA
class Idioma(models.Model):
    id = models.AutoField(auto_created=True ,primary_key= True, serialize=False,verbose_name='ID')
    idioma = models.CharField (max_length=200, null=True)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.idioma

# COMPETENCIA
class Compentencia(models.Model):
    id = models.AutoField(auto_created=True ,primary_key= True, serialize=False,verbose_name='ID')
    descripCompetencia = models.CharField(max_length=200, null=True, verbose_name="Competencia")
    estado = models.BooleanField(default=False, verbose_name="Disponible")

    def __str__(self):
        return self.descripCompetencia

# CAPACITACION
class Capacitacion(models.Model):
    NIVEL ={
        ('Grado', 'Grado'),
        ('Post-grado', 'Post-grado'),
        ('Maestría', 'Maestría'),
        ('Doctorado', 'Doctorado'),
        ('Técnico', 'Técnico'),
        ('Gestión', 'Gestión'),
    }
    id = models.AutoField(auto_created=True ,primary_key= True, serialize=False,verbose_name='ID')
    capacitacion = models.CharField(max_length=50, null=True)
    descripcion = models.CharField(max_length=200, null=True)
    nivel = models.CharField(max_length=12, null=True, choices= NIVEL)
    fechaDesde = models.DateField()
    fechaHasta = models.DateField()
    institucion = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.capacitacion

# PUESTO
class Puesto(models.Model):
    NIVELRIESGO ={
        ('Alto', 'Alto'),
        ('Medio', 'Medio'),
        ('Bajo', 'Bajo'),
    }
    id = models.AutoField(auto_created=True ,primary_key= True, serialize=False,verbose_name='ID')
    puesto =  models.CharField(max_length=50, null=True)
    nivelRiesgo = models.CharField(max_length=5, null=True, choices=NIVELRIESGO)
    nivelMinimoSalario = models.DecimalField(max_digits=10, decimal_places=2)
    nivelMaximoSalario = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.puesto

# EXPERIENCIA LABORAL
class ExperienciaLaboral(models.Model):
    id = models.AutoField(auto_created=True ,primary_key= True, serialize=False,verbose_name='ID')
    empresa = models.CharField (max_length=200, null=True)
    puestoOcupado = models.CharField(max_length=200, null=True)
    fechaDesde = models.DateField()
    fechaHasta = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.puestoOcupado

# EMPLEADO      
class Empleado(models.Model):
    id = models.AutoField(auto_created=True ,primary_key= True, serialize=False,verbose_name='ID')
    nombre = models.CharField (max_length=60, null=True)
    cedula = models.IntegerField(max_length=10, null=True)
    fechaIngreso = models.DateField()
    departamento = models.CharField(max_length=50, null=True)
    puesto = models.OneToOneField(Puesto, on_delete=models.CASCADE)
    salarioMensual = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=False) 

    def __str__(self):
        return self.nombre

# CANDIDATO 
class Candidato(models.Model):
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
    id = models.AutoField(auto_created=True ,primary_key= True, serialize=False,verbose_name='ID')
    nombre = models.CharField (max_length=60, null=True)
    cedula = models.IntegerField(max_length=10, null=True)
    puestoAspira = models.ForeignKey(Puesto, on_delete=models.CASCADE, null=True)
    departamento = models.CharField(max_length=60, null=True)
    salarioAspira = models.DecimalField(max_digits=10, decimal_places=2)
    principalesCompetencia = models.ManyToManyField(Compentencia)
    principalesCapacitacion = models.ManyToManyField(Capacitacion)
    expeiencia = models.ManyToManyField(ExperienciaLaboral)
    recomendacion = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True)
    
