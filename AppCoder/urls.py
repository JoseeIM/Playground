from django.urls import path 
from AppCoder import views
urlpatterns = [
    path('', views.inicio,name="Inicio"),
    path('Cursos', views.cursos),
    path('Estudiantes', views.estudiantes),
    path('Profesores', views.profesores),
    path('Entregables', views.entregables),
    #path('FormularioC', views.formularioC),#formularioC=FormularioCurso(La C al final hace referencia a que tipo de formulario es por eso al final puse una C referiendome a "Curso")#
    #path('FormularioP', views.formularioP),
    path('BusquedaCamada', views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
]
