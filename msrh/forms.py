from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Compentencia
        fields = '__all__'
        widgets = {
            'descripCompetencia':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ej:. Trabajo en Equipo...'}),
            'estado':forms.CheckboxInput(attrs={'class':'form-check-input'})
        }

class IdiomaForm(forms.ModelForm):
    class Meta:
        model = Idioma
        fields = '__all__'
        widgets = {
            'idioma':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ej:. Español...'}),
            'estado':forms.CheckboxInput(attrs={'class':'form-check-input'})
        }

class CapacitacionForm(forms.ModelForm):
    class Meta:
        model = Capacitacion
        fields = '__all__'
        widgets = {
            'capacitacion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Formación laboral'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ej:. En que consiste esa capacitacion...'}),
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
            'puesto': forms.TextInput(attrs={'class': 'form-control ', 'placeholder':'Ej:. Programador...'}),
            'nivelRiesgo': forms.Select(attrs={'class':'form-select'}),
            'nivelMinimoSalario': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'$ 0.00'}),
            'nivelMaximoSalario': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'$ 0.00'}),
            'estado': forms.CheckboxInput(attrs={'class':'form-check-input', 'Disponible':'$ 0.00'}),
        }

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control','placeholder':'xxx-xxxxxxx-x'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese su nombre completo'}),
            'puestoAspira': forms.Select(attrs={'class': 'form-select'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
            'salarioAspira': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'$ 0.00'}),
            'principalesCompetencia': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'principalesCapacitacion': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'expeiencia': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'recomendacion': forms.Select(attrs={'class': 'form-select'}),
            'idioma': forms.SelectMultiple(attrs={'class': 'form-check-input'}),
        }

class ExperienciaLaboralForm(forms.ModelForm):
    class Meta:
        model = ExperienciaLaboral
        fields = '__all__'
        widgets = {
            'empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Institucion o empresa donde estuvo'} ),
            'puestoOcupado': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ej:. Programador...'}),
            'fechaDesde': forms.DateInput(attrs={'class': 'form-control', 'type':'date' }),
            'fechaHasta': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'$ 0.00'}),
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese su nombre completo'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'xxx-xxxxxxx-x'}),
            'puestoOcupado': forms.Select(attrs={'class': 'form-select'}),
            'fechaIngreso': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto': forms.Select(attrs={'class': 'form-select'}),
            'salarioMensual': forms.NumberInput(attrs={'class': 'form-select', 'placeholder':'$ 0.00'}),
            'estado': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
