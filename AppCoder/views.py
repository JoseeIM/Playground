from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso,Profesor,Estudiante,Entregable
from AppCoder.forms import FormularioCurso,FormularioProfesor,FormularioEntregable,FormularioEstudiante
def inicio(request):
    return render (request,"AppCoder/inicio.html")
def cursos(request):
    return render (request,"AppCoder/cursos.html")
def estudiantes(request):
    return render (request,"AppCoder/estudiantes.html")
def profesores(request):
    return render (request,"AppCoder/profesores.html")
def entregables(request):
    return render (request,"AppCoder/entregables.html")
def cursos(request):
    ##FormularioCurso
    if request.method == 'POST':
        miFormulario= FormularioCurso(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            curso= Curso (nombre=informacion['curso'], comision=informacion['comision'] )
            curso.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario=FormularioCurso()
    return render (request,"AppCoder/cursos.html",{"miFormulario":miFormulario})
def profesores(request):
    ##FormularioProfesor
    if request.method == 'POST':
        miFormulario= FormularioProfesor(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            profesor= Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'] )
            profesor.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario=FormularioProfesor()
    return render (request,"AppCoder/profesores.html",{"miFormulario":miFormulario})
def estudiantes(request):
    ##FormularioEstudiantes
    if request.method == 'POST':
        miFormulario= FormularioEstudiante(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            estudiante= Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            estudiante.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario=FormularioEstudiante()
    return render (request,"AppCoder/estudiantes.html",{"miFormulario":miFormulario})
def entregable(request):
    ##FormularioEntregable
    if request.method == 'POST':
        miFormulario= FormularioEntregable(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            entregable= Entregable (nombre=informacion['nombre'], FechaDeEntrega=informacion['FechaDeEntrega'], entregado=informacion['entregado'])
            entregable.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario=FormularioEntregable()
    return render (request,"AppCoder/entregable.html",{"miFormulario":miFormulario})

def busquedaCamada(request):
    return render (request,"AppCoder/busquedaCamada.html")
def buscar(request):
    if request.GET['comision']:
        comision=request.GET['comision']
        cursos=Curso.objects.filter(comision__icontains=comision)
        return render(request,"AppCoder/inicio.html",{"cursos":cursos,"comision":comision})
    else:
        respuesta="No enviaste datos"
    return render(request,"AppCoder/cursos.html",{"respuesta":respuesta})
# Create your views here.
