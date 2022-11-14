from django.urls import path 
from AppCoder import views
urlpatterns = [
    path('', views.inicio),
    path('Cursos', views.cursos),
    path('Estudiantes', views.estudiantes),
    path('Profesores', views.profesores),
    path('Entregables', views.entregables),
]
