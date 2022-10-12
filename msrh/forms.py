from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Compentencia
        fields = '__all__'
        widgets = {
            'descripCompetencia':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.CheckboxInput(attrs={'class':'form-check-input'})
        }

class IdiomaForm(forms.ModelForm):
    class Meta:
        model = Idioma
        fields = '__all__'
        widgets = {
            'idioma':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.CheckboxInput(attrs={'class':'form-check-input'})
        }

class CapacitacionForm(forms.ModelForm):
    class Meta:
        model = Capacitacion
        fields = '__all__'
        widgets = {
            'capacitacion':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'nivel':forms.Select(attrs={'class':'form-select'}),
            'fechaDesde':forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            'fechaHasta':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'institucion':forms.TextInput(attrs={'class':'form-control'}),
        }

class PuestoForm(forms.ModelForm):
    class Meta:
        model = Puesto
        fields = '__all__' #['']
        widgets = {
            'puesto': forms.TextInput(attrs={'class': 'form-control '}),
            'nivelRiesgo': forms.Select(attrs={'class':'form-select'}),
            'nivelMinimoSalario': forms.NumberInput(attrs={'class':'form-control'}),
            'nivelMaximoSalario': forms.NumberInput(attrs={'class':'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = '__all__'
        widgets = {
            'cedula': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'puestoAspira': forms.Select(attrs={'class': 'form-select'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
            'salarioAspira': forms.NumberInput(attrs={'class': 'form-control'}),
            'principalesCompetencia': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'principalesCapacitacion': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'expeiencia': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'recomendacion': forms.Select(attrs={'class': 'form-select'}),
        }

class ExperienciaLaboralForm(forms.ModelForm):
    class Meta:
        model = ExperienciaLaboral
        fields = '__all__'
        widgets = {
            'empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'name@example.com'} ),
            'puestoOcupado': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaDesde': forms.DateInput(attrs={'class': 'form-control'}),
            'fechaHasta': forms.DateInput(attrs={'class': 'form-control'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.NumberInput(attrs={'class': 'form-control'}),
            'puestoOcupado': forms.Select(attrs={'class': 'form-select'}),
            'fechaIngreso': forms.DateInput(attrs={'class': 'form-control'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto': forms.Select(attrs={'class': 'form-select'}),
            'salarioMensual': forms.NumberInput(attrs={'class': 'form-select'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
