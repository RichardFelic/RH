# Basico
from datetime import datetime
import datetime
from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from msrh.forms import *
from msrh.models import *
import datetime

# HttpResponse
from http.client import HTTPResponse
from django.shortcuts import HttpResponse
from django.http import HttpResponse

# Permisos | Roles | Autenticacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

#Excel
import csv

# Create your views here.

#Crear exportacion
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Empledos.csv'

    writer = csv.writer(response)
    
    empleado = Empleado.objects.all()
    
    writer.writerow(['Nombre', 'Cedula', 'Fecha de Ingreso', 'Departamento', 'Puesto', 'Salario Mensual', 'Estado'])

    for empleado in empleado:
        writer.writerow([empleado.nombre, empleado.cedula, empleado.fechaIngreso, empleado.departamento, empleado.puesto, empleado.salarioMensual, empleado.estado])
    return response 

#Home
@login_required(login_url='login')
@admin_only
def home(request):
    puesto = Puesto.objects.all()
    candidato = Candidato.objects.filter(createdBy=request.user).count()
    empleado = Empleado.objects.all()

    num_empleado = empleado.count()
    total_puesto = puesto.count()

    context = {'total_puesto':total_puesto, 'candidato':candidato, 'num_empleado':num_empleado}
    return render(request, 'msrh/dashboard.html', context)

#Competencia
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def competencia(request):
    competencia = Compentencia.objects.all()
    return render(request, 'msrh/competencia.html', {'competencia':competencia})

#Idioma
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def idioma(request):
    idioma = Idioma.objects.all()
    return render(request, 'msrh/idioma.html', {'idioma':idioma})

#Capacitacion
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','candidato'])
def capacitacion(request):
    capacitacion = Capacitacion.objects.all()
    return render(request, 'msrh/capacitacion.html', {'capacitacion':capacitacion})

#Puesto
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def puesto(request):
    puesto = Puesto.objects.all()
    return render(request, 'msrh/puesto.html', {'puesto':puesto})

#candidato
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','candidato'])
def candidato(request):
    candidato = Candidato.objects.all()
    return render(request, 'msrh/candidato.html', {'candidato':candidato})
    
#Experiencia Laboral
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','candidato'])
def experienciaLaboral(request):
    experiencialaboral = ExperienciaLaboral.objects.all()
    return render(request, 'msrh/experienciaLaboral.html', {'experiencialaboral':experiencialaboral})

#Empleado
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def empleado(request):
    empleado = Empleado.objects.all()
    return render(request, 'msrh/empleado.html', {'empleado':empleado})

#AGREGAR PUESTO
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_Puesto(request):
    form = PuestoForm()
    if request.method == "POST":
        form = PuestoForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('/puesto')
        
    return render(request, 'msrh/CRUD/Crearpuesto.html', {'form':form})

#EDITAR PUESTO
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_Puesto(request, pk):
    pk = str(pk)
    try:
        puesto = Puesto.objects.get(id=pk)
    except Puesto.DoesNotExist:
        return redirect('/puesto')
    form = PuestoForm(request.POST or None, instance=puesto)
    if form.is_valid():
        form.save()
        return redirect('/puesto')
    context = {'form':form, 'puesto':puesto}
    return render(request, 'msrh/CRUD/Editarpuesto.html', context)

#Borrar Puesto
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_Puesto(request, pk):             
    puesto = Puesto.objects.get(id=pk)
    if request.method == 'POST':
        puesto.delete()
        return redirect('/puesto')
    context = {'puesto':puesto}
    return render(request, 'msrh/CRUD/Borrarpuesto.html', context)               

#Detalles Puesto
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def detail_Puesto(request, pk):
    puesto = Puesto.objects.get(id=pk)
    context = {'puesto':puesto}
    return render(request, 'msrh/CRUD/Detallespuesto.html', context)   

#Agregar Compe
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_Compe(request):
    form_compe = CompetenciaForm()
    if request.method == "POST":
        form_compe = CompetenciaForm(request.POST or None)
        if form_compe.is_valid():
                form_compe.save()
                return redirect('/competencia')
        
    return render(request, 'msrh/CRUD/Crearcompe.html', {'form_compe':form_compe})


#Editar Compe    
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_Compe(request, pk):
    pk = str(pk)
    try:
        compe = Compentencia.objects.get(id=pk)
    except Compentencia.DoesNotExist:
        return redirect('/competencia')
    form_compe = CompetenciaForm(request.POST or None, instance=compe)
    if form_compe.is_valid():
        form_compe.save()
        return redirect('/competencia')
    context = {'form_compe':form_compe, 'compe':compe}
    return render(request, 'msrh/CRUD/Editarcompe.html', context)

#Borrar Compe
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_Compe(request, pk):             
    compe = Compentencia.objects.get(id=pk)
    if request.method == 'POST':
        compe.delete()
        return redirect('/competencia')
    context = {'compe':compe}
    return render(request, 'msrh/CRUD/Borrarcompe.html', context)   

#Detalles Competencia
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def detail_Compe(request, pk):
    compe = Compentencia.objects.get(id=pk)
    context = {'compe':compe}
    return render(request, 'msrh/CRUD/Detallescompe.html', context)   

#Crear Idioma
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_Idioma(request):
    form = IdiomaForm()
    if request.method == "POST":
        form = IdiomaForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('/idioma')
        
    
    return render(request, 'msrh/CRUD/Crearidioma.html', {'form':form})

#Editar Idioma  
@login_required(login_url='login') 
@allowed_users(allowed_roles=['admin'])
def update_Idioma(request, pk):
    pk = str(pk)
    try:
        idioma = Idioma.objects.get(id=pk)
    except Idioma.DoesNotExist:
        return redirect('/idioma')
    form = IdiomaForm(request.POST or None, instance=idioma)
    if form.is_valid():
        form.save()
        return redirect('/idioma')
    context = {'form':form, 'idioma':idioma}
    return render(request, 'msrh/CRUD/Editaridioma.html', context)

#Borrar Idioma
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_Idioma(request, pk):             
    idioma = Idioma.objects.get(id=pk)
    if request.method == 'POST':
        idioma.delete()
        return redirect('/idioma')
    context = {'idioma':idioma}
    return render(request, 'msrh/CRUD/Borraridioma.html', context)   

#Detalles Idioma
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def detail_Idioma(request, pk):
    idioma = Idioma.objects.get(id=pk)
    context = {'idioma':idioma}
    return render(request, 'msrh/CRUD/Detallesidioma.html', context)  

#Crear Experiencia Laboral
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'candidato'])
def add_ExperienciaLaboral(request):
    form = ExperienciaLaboralForm()
    if request.method == "POST":
        form = ExperienciaLaboralForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('/experienciaLaboral')
    
    return render(request, 'msrh/CRUD/Crearexperiencialaboral.html', {'form':form})

#Editar Experiencia Laboral
@login_required(login_url='login')   
@allowed_users(allowed_roles=['admin', 'candidato'])
def update_ExperienciaLaboral(request, pk):
    pk = str(pk)
    try:
        experienciaLaboral = ExperienciaLaboral.objects.get(id=pk)
    except Idioma.DoesNotExist:
        return redirect('/experienciaLaboral')
    form = ExperienciaLaboralForm(request.POST or None, instance=experienciaLaboral)
    if form.is_valid():
        form.save()
        return redirect('/experienciaLaboral')
    context = {'form':form, 'experienciaLaboral':experienciaLaboral}
    return render(request, 'msrh/CRUD/Editarexperiencialaboral.html', context)

#Borrar Experiencia Laboral
@login_required(login_url='login') 
@allowed_users(allowed_roles=['admin', 'candidato'])  
def delete_ExperienciaLaboral(request, pk):             
    experienciaLaboral = ExperienciaLaboral.objects.get(id=pk)
    if request.method == 'POST':
        experienciaLaboral.delete()
        return redirect('/experienciaLaboral')
    context = {'experienciaLaboral':experienciaLaboral}
    return render(request, 'msrh/CRUD/Borrarexperiencialaboral.html', context)   

#Detalles Experiencia Laboral
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'candidato'])  
def detail_ExperienciaLaboral(request, pk):
    experienciaLaboral = ExperienciaLaboral.objects.get(id=pk)
    context = {'experienciaLaboral':experienciaLaboral}
    return render(request, 'msrh/CRUD/Detallesexperiencialaboral.html', context) 

#Crear Capacitacion
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','candidato'])
def add_Capacitacion(request):
    form = CapacitacionForm()
    if request.method == "POST":
        form = CapacitacionForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('capacitacion')
        

    return render(request, 'msrh/CRUD/Crearcapacitacion.html', {'form':form})

#Editar Capacitacion
@login_required(login_url='login')  
@allowed_users(allowed_roles=['admin', 'candidato']) 
def update_Capacitacion(request, pk):
    pk = str(pk)
    try:
        capacitacion = Capacitacion.objects.get(id=pk)
    except Capacitacion.DoesNotExist:
        return redirect('/capacitacion')
    form = CapacitacionForm(request.POST or None, instance=capacitacion)
    if form.is_valid():
        form.save()
        return redirect('/capacitacion')
    context = {'form':form, 'capacitacion':capacitacion}
    return render(request, 'msrh/CRUD/Editarcapacitacion.html', context)

#Borrar Capacitacion
@login_required(login_url='login')  
@allowed_users(allowed_roles=['admin', 'candidato']) 
def delete_Capacitacion(request, pk):             
    capacitacion = Capacitacion.objects.get(id=pk)
    if request.method == 'POST':
        capacitacion.delete()
        return redirect('/capacitacion')
    context = {'capacitacion':capacitacion}
    return render(request, 'msrh/CRUD/Borrarcapacitacion.html', context)   

#Detalles Capacitacion
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'candidato'])
def detail_Capacitacion(request, pk):
    capacitacion = Capacitacion.objects.get(id=pk)
    context = {'capacitacion':capacitacion}
    return render(request, 'msrh/CRUD/Detallescapacitacion.html', context) 

#Crear Empleado
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_Empleado(request):
    form = EmpleadoForm()
    if request.method == "POST":
        form = EmpleadoForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('/empleado')
    
    return render(request, 'msrh/CRUD/Crearempleado.html', {'form':form})

#Editar Empleado
@login_required(login_url='login')   
@allowed_users(allowed_roles=['admin'])
def update_Empleado(request, pk):
    pk = str(pk)
    try:
        empleado = Empleado.objects.get(id=pk)
    except Empleado.DoesNotExist:
        return redirect('/empleado')
    form = EmpleadoForm(request.POST or None, instance=empleado)
    if form.is_valid():
        form.save()
        return redirect('/empleado')
    context = {'form':form, 'empleado':empleado}
    return render(request, 'msrh/CRUD/Editarempleado.html', context)

#Borrar Empleado
@login_required(login_url='login') 
@allowed_users(allowed_roles=['admin'])  
def delete_Empleado(request, pk):             
    empleado = Empleado.objects.get(id=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('/empleado')
    context = {'empleado':empleado}
    return render(request, 'msrh/CRUD/Borrarempleado.html', context)   

#Detalles Empleado
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def detail_Empleado(request, pk):
    empleado = Empleado.objects.get(id=pk)
    context = {'empleado':empleado}
    return render(request, 'msrh/CRUD/Detallesempleado.html', context) 

#Crear Candidato
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','candidato'])
def add_Candidato(request):
    form = CandidatoForm()
    if request.method == "POST":
        form = CandidatoForm(request.POST or None)
        form.instance.createdBy = request.user
        if form.is_valid():
                form.save()
                return redirect('/candidato')
        
    
    return render(request, 'msrh/CRUD/Crearcandidato.html', {'form':form})
    
#Editar Candidato
@login_required(login_url='login')   
@allowed_users(allowed_roles=['admin','candidato'])
def update_Candidato(request, pk):
    pk = str(pk)
    try:
        candidato = Candidato.objects.get(id=pk)
    except Candidato.DoesNotExist:
        return redirect('/candidato')
    form = CandidatoForm(request.POST or None, instance=candidato)
    if form.is_valid():
        form.save()
        return redirect('/candidato')
    context = {'form':form, 'candidato':candidato}
    return render(request, 'msrh/CRUD/Editarcandidato.html', context)

#Borrar Candidato
@login_required(login_url='login')  
@allowed_users(allowed_roles=['admin','candidato']) 
def delete_Candidato(request, pk):             
    candidato = Candidato.objects.get(id=pk)
    if request.method == 'POST':
        candidato.delete()
        return redirect('/candidato')
        
    context = {'candidato':candidato}
    return render(request, 'msrh/CRUD/Borrarcandidato.html', context)   

#Detalles Candidato
@login_required(login_url='login') 
@allowed_users(allowed_roles=['admin','candidato'])
def detail_Candidato(request, pk):
    candidato = Candidato.objects.get(id=pk)
    context = {'candidato':candidato}
    return render(request, 'msrh/CRUD/Detallescandidato.html', context) 
    
#Login
@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.info(request, 'El Nombre de Usuario o la Contraseña está incorrecta')
            
    context={}
    return render(request, 'msrh/LoginRegister/login.html', context)

#Logout
def logoutUser(request):
    logout(request)
    return redirect('login')
 
#Register
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='candidato')
            user.groups.add(group)

            messages.success(request, 'Account was created for' + username)
            return redirect('/login') 

    context={'form':form}
    return render(request, 'msrh/LoginRegister/register.html', context)

#User
@login_required(login_url='login')
@allowed_users(allowed_roles=['candidato'])
def userPage(request):
    #candidatos = Candidato.objects.filter(createdBy=request.user)
    candidato = Candidato.objects.filter(createdBy=request.user)

    #context={'candidato': candidato}
    return render(request,'msrh/user.html', {'candidato':candidato})

#Proceso de Candidato a Empleado
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def candidatoProceso(request, pk):
    candidato = Candidato.objects.filter(id=pk)
    try:
        for i in candidato:
            Empleado.objects.create(
                nombre=i.nombre, cedula=i.cedula, fechaIngreso=datetime.datetime.now(),
                departamento=i.departamento, puesto=i.puestoAspira, salarioMensual=i.salarioAspira,
                estado=True
            )
        Candidato.objects.filter(id=pk).delete()
    except IntegrityError:
        messages.error(request, "El candidadto ya esta seleccionado como empleado.")
        return redirect('candidato')
    return redirect('empleado')