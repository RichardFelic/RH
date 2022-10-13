from email.policy import default
from random import choices
from re import S
from secrets import choice
from tabnanny import verbose
from tkinter import CASCADE
from django.core.exceptions import ValidationError
import datetime
from django.db import models
from django.contrib.auth.models import User

from msrh.validarcedula import validar_cedula

# Create your models here.

# IDIOMA
class Idioma(models.Model):
    id = models.AutoField(auto_created=True ,primary_key= True, serialize=False,verbose_name='ID')
    idioma = models.CharField (max_length=200, null=True, verbose_name='Idioma')
    estado = models.BooleanField(default=False, verbose_name='Disponible')

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
    capacitacion = models.CharField(max_length=50, null=True, verbose_name='Capacitación')
    descripcion = models.CharField(max_length=200, null=True, verbose_name='Descripción')
    nivel = models.CharField(max_length=12, null=True, choices= NIVEL, verbose_name='Nivel')
    fechaDesde = models.DateField(verbose_name='Fecha Desde')
    fechaHasta = models.DateField(verbose_name='Fecha Hasta')
    institucion = models.CharField(max_length=50, null=True, verbose_name='Institución')
    
    def __str__(self):
        return self.capacitacion
    
    def clean(self, *args, **kwargs):
        super(Capacitacion, self).clean(*args, **kwargs)

        if self.capacitacion == '' or self.descripcion == '' or self.institucion == '':
            raise ValidationError(
             {'Los campos estan vacios.'}
        )

        if self.fechaHasta < self.fechaDesde:
            raise ValidationError(
                {'fechaHasta': 'La fecha final no puede ser menor a la inicial.'}
        )

# PUESTO
class Puesto(models.Model):
    NIVELRIESGO ={
        ('Alto', 'Alto'),
        ('Medio', 'Medio'),
        ('Bajo', 'Bajo'),
    }
    id = models.AutoField(auto_created=True ,primary_key= True, serialize=False,verbose_name='ID')
    puesto =  models.CharField(max_length=50, null=True, verbose_name='Puesto')
    nivelRiesgo = models.CharField(max_length=5, null=True, choices=NIVELRIESGO, verbose_name='Nivel Riesgo')
    nivelMinimoSalario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Salario Mínimo')
    nivelMaximoSalario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Salario Máximo')
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.puesto
    
    def clean(self): 
        if self.nivelMaximoSalario <= self.nivelMinimoSalario:
            raise ValidationError(
                {'nivelMaximoSalario': "El Salario Maximo no puede ser menor o igual al minimo."}
            ) 

        if self.nivelMaximoSalario <=0 or self.nivelMinimoSalario <=0:
            raise ValidationError(
                {'El salario no puede ser negativo o neutro.'}
            )

# EXPERIENCIA LABORAL
class ExperienciaLaboral(models.Model):
    id = models.AutoField(auto_created=True ,primary_key= True, serialize=False,verbose_name='ID')
    empresa = models.CharField (max_length=200, null=True, verbose_name='Empresa')
    puestoOcupado = models.CharField(max_length=200, null=True, verbose_name='Puesto Ocupado')
    fechaDesde = models.DateField(verbose_name='Fecha Desde')
    fechaHasta = models.DateField(verbose_name='Fecha Hasta')
    salario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Salario')
    def __str__(self):
        return self.puestoOcupado
    
    def clean(self, *args, **kwargs):
        if self.empresa == '' or self.puestoOcupado == '':
            raise ValidationError(
               {'Los campos estan vacios.'} 
            )

        if self.fechaHasta < self.fechaDesde:
            raise ValidationError(
                {'fechaHasta': 'La fecha final no puede ser menor a la inicial.'}
            )
    
    

# EMPLEADO      
class Empleado(models.Model):
    id = models.AutoField(auto_created=True ,primary_key= True, serialize=False,verbose_name='ID')
    nombre = models.CharField (max_length=60, null=True, verbose_name='Nombre completo')
    cedula = models.CharField(max_length=13, null=True, verbose_name='Cédula')
    fechaIngreso = models.DateField(auto_now_add=False, null=True)
    departamento = models.CharField(max_length=50, null=True)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE,null=True, verbose_name='Empresa')
    salarioMensual = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Salario Mensual')
    estado = models.BooleanField(default=False, verbose_name='Disponible') 

    def __str__(self):
        return self.nombre
    
    def clean(self):
        if validar_cedula(self.cedula) == False: 
            raise ValidationError(
                {'cedula': 'La cedula es incorrecta'}
            )

# CANDIDATO 
class Candidato(models.Model):
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
    id = models.AutoField(auto_created=True ,primary_key= True, serialize=False,verbose_name='ID')
    nombre = models.CharField (max_length=60, null=True, verbose_name='Nombre Completo')
    cedula = models.CharField(max_length=13, null=True, verbose_name='Cédula')
    puestoAspira = models.ForeignKey(Puesto, on_delete=models.CASCADE, null=True,verbose_name='Puesto que Aspira')
    departamento = models.CharField(max_length=60, null=True, verbose_name='Departamento')
    salarioAspira = models.DecimalField(max_digits=10, decimal_places=2)
    principalesCompetencia = models.ManyToManyField(Compentencia, verbose_name='Principales Competencias')
    principalesCapacitacion = models.ManyToManyField(Capacitacion, verbose_name='Principales ')
    expeiencia = models.ManyToManyField(ExperienciaLaboral, verbose_name='Experiencia Laboral')
    recomendacion = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, verbose_name='Recomendado por')
    def str(self):
        return self.nombre

    def clean(self):
        if validar_cedula(self.cedula) == False: 
            raise ValidationError(
                {'cedula': 'La cedula es incorrecta'}
            )