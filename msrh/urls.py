from django.shortcuts import render 
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    #Views principales
    path('', views.home, name='home'),
    path('competencia/', views.competencia,  name='competencia'),
    path('idioma/', views.idioma, name='idioma'),
    path('capacitacion/', views.capacitacion, name='capacitacion'),
    path('puesto/', views.puesto, name='puesto'),
    path('candidato/', views.candidato, name='candidato'),
    path('experienciaLaboral/', views.experienciaLaboral, name='experienciaLaboral'),
    path('empleado/', views.empleado, name='empleado'),
    path('registrarIdioma/', views.registrarIdioma),
    
    #Competición CRUD
    path('Crearcompe/', views.add_Compe, name='Crearcompe'),
    path('Borrarcompe/<str:pk>/', views.delete_Compe, name='Borrarcompe'),
    path('Editarcompe/<str:pk>/', views.update_Compe, name='Editarcompe'),
    path('Detallescompe/<str:pk>/', views.detail_Compe, name='Detallescompe'),
    
    #Puesto CRUD
    path('Crearpuesto/', views.add_Puesto, name='Crearpuesto'),
    path('Editarpuesto/<str:pk>/', views.update_Puesto, name='Editarpuesto'),
    path('Borrarpuesto/<str:pk>/', views.delete_Puesto, name='Borrarpuesto'),
    path('Detallespuesto/<str:pk>', views.detail_Puesto, name='Detallespuesto'),

    #Idioma CRUD
    path('Crearidioma/', views.add_Idioma, name='Crearidioma'),
    path('Editaridioma/<str:pk>/', views.update_Idioma, name='Editaridioma'),
    path('Borraridioma/<str:pk>/', views.delete_Idioma, name='Borraridioma'),
    path('Detallesidioma/<str:pk>', views.detail_Idioma, name='Detallesidioma'),
    
    #Capacitacion CRUD
    path('Crearcapacitacion/', views.add_Capacitacion, name='Crearcapacitacion'),
    path('Editarcapacitacion/<str:pk>/', views.update_Capacitacion, name='Editarcapacitacion'),
    path('Borrarcapacitacion/<str:pk>/', views.delete_Capacitacion, name='Borrarcapacitacion'),
    path('Detallescapacitacion/<str:pk>', views.detail_Capacitacion, name='Detallescapacitacion'),  

    #Experiecia Laboral CRU
    path('Crearexperiencialaboral/', views.add_ExperienciaLaboral, name='Crearexperiencialaboral'),
    path('Editarexperiencialaboral/<str:pk>/', views.update_ExperienciaLaboral, name='Editarexperiencialaboral'),
    path('Borrarexperiencialaboral/<str:pk>/', views.delete_ExperienciaLaboral, name='Borrarexperiencialaboral'),
    path('Detallesexperiencialaboral/<str:pk>', views.detail_ExperienciaLaboral, name='Detallesexperiencialaboral'),

   #Empleado CRUD
    path('Crearempleado/', views.add_Empleado, name='Crearempleado'),
    path('Editarempleado/<str:pk>/', views.update_Empleado, name='Editarempleado'),
    path('Borrarempleado/<str:pk>/', views.delete_Empleado, name='Borrarempleado'),
    path('Detallesempleado/<str:pk>', views.detail_Empleado, name='Detallesempleado'),   

    #Candidato CRUD
    path('Crearcandidato/', views.add_Candidato, name='Crearcandidato'),
    path('Editarcandidato/<str:pk>/', views.update_Candidato, name='Editarcandidato'),
    path('Borrarcandidato/<str:pk>/', views.delete_Candidato, name='Borrarcandidato'),
    path('Detallescandidato/<str:pk>', views.detail_Candidato, name='Detallescandidato'), 

    #Login and Register
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    #User
    path('user/', views.userPage, name='user'),

    #PDF
    path('pdf/', views.pdf, name='pdf'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)