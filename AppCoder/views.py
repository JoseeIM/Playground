from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso,Profesor,Estudiante,Entregable
from AppCoder.forms import FormularioCurso,FormularioProfesor,FormularioEntregable,FormularioEstudiante
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
def inicio(request):
    return render (request,"AppCoder/inicio.html")
def cursos(request):
    return render (request,"AppCoder/cursos.html")
def estudiantes(request):
    return render (request,"AppCoder/estudiantes.html")
def profesores(request):
    return render (request,"AppCoder/profesor.html")
def entregables(request):
    return render (request,"AppCoder/entregables.html")
def CreacionCurso(request):##FormularioCurso
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
    return render (request,"AppCoder/CursosCreacion.html",{"miFormulario":miFormulario})
def CreacionProfesor(request):##FormularioProfesor
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
    return render (request,"AppCoder/ProfesorCreacion.html",{"miFormulario":miFormulario})
def CreacionEstudiantes(request):##FormularioEstudiantes
    if request.method == 'POST':
        miFormulario= FormularioEstudiante(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            estudiantes= Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'],email=informacion['email'] )
            estudiantes.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario=FormularioEstudiante()
    return render (request,"AppCoder/EstudiantesCreacion.html",{"miFormulario":miFormulario})
def CreacionEntregables(request):##FormularioEntregable
    if request.method == 'POST':
        miFormulario= FormularioEntregable(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            entregable= Entregable (nombre=informacion['nombre'], FechaDeEntrega=informacion['Fecha_De_Entrega'],entregado=informacion['entregado'] )
            entregable.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario=FormularioEntregable()
    return render (request,"AppCoder/EntregablesCreacion.html",{"miFormulario":miFormulario})
def BuscadorCurso(request):#BusquedaDeCursos
    if request.GET.get('comision', False):
        comision=request.GET['comision']
        cursos=Curso.objects.filter(comision__icontains=comision)
        return render(request,"AppCoder/CursosBuscador.html",{"cursos":cursos,"comision":comision})
    else:
        respuesta="No enviaste datos"
    return render(request,"AppCoder/CursosBuscador.html",{"respuesta":respuesta})
def BuscadorEstudiantes(request):#BusquedaDeEstudiantes
    if request.GET.get('apellido', False):
        apellido=request.GET['apellido']
        estudiantes=Estudiante.objects.filter(apellido__icontains=apellido)
        return render(request,"AppCoder/EstudiantesBuscador.html",{"estudiantes":estudiantes,"apellido":apellido})
    else:
        respuesta="No enviaste datos"
    return render(request,"AppCoder/EstudiantesBuscador.html",{"respuesta":respuesta})
def BuscadorProfesor(request):#BusquedaDeProfesorS
    if request.GET.get('apellido', False):
        apellido=request.GET['apellido']
        profesores=Profesor.objects.filter(apellido__icontains=apellido)
        return render(request,"AppCoder/ProfesorBuscador.html",{"profesores":profesores,"apellido":apellido})
    else:
        respuesta="No enviaste datos"
    return render(request,"AppCoder/ProfesorBuscador.html",{"respuesta":respuesta})
def BuscadorEntregables(request):#BusquedaDeEntregables
    if request.GET.get('nombre', False):
        nombre=request.GET['nombre']
        entregables=Entregable.objects.filter(nombre__icontains=nombre)
        return render(request,"AppCoder/EntregablesBuscador.html",{"entregables":entregables,"nombre":nombre})
    else:
        respuesta="No enviaste datos"
    return render(request,"AppCoder/EntregablesBuscador.html",{"respuesta":respuesta})
##MODIFICACIONES PARA EL CURSO##
class CursoList(ListView):
    model=Curso
    template_name="AppCoder/curso_list.html"
class CursoDetalle(DetailView):
    model=Curso
    template_name="AppCoder/curso_detalle.html"
class CursoCreacion(CreateView):
    model=Curso
    success_url="/curso/list"
    fields=['nombre','comision']
class CursoUpdate(UpdateView):
    model=Curso
    success_url="/curso/list"
    fields=['nombre','comision']
class CursoDelete(DeleteView):
    model=Curso
    success_url="/curso/list"
##MODIFICACIONES PARA ESTUDIANTES##
class EstudianteList(ListView):
    model=Estudiante
    template_name="AppCoder/estudiante_list.html"
class EstudianteDetalle(DetailView):
    model=Estudiante
    template_name="AppCoder/estudiante_detalle.html"
class EstudianteCreacion(CreateView):
    model=Estudiante
    success_url="/estudiante/list"
    fields=['nombre','apellido','email']
class EstudianteUpdate(UpdateView):
    model=Estudiante
    success_url="/estudiante/list"
    fields=['nombre','apellido','email']
class EstudianteDelete(DeleteView):
    model=Estudiante
    success_url="/estudiante/list"
##MODIFICACIONES PARA PORFESOR##
class ProfesorList(ListView):
    model=Profesor
    template_name="AppCoder/profesor_list.html"
class ProfesorDetalle(DetailView):
    model=Profesor
    template_name="AppCoder/profesor_detalle.html"
class ProfesorCreacion(CreateView):
    model=Profesor
    success_url="/profesor/list"
    fields=['nombre','apellido','email','profesion']
class ProfesorUpdate(UpdateView):
    model=Profesor
    success_url="/profesor/list"
    fields=['nombre','apellido','email','profesion']
class ProfesorDelete(DeleteView):
    model=Profesor
    success_url="/entregable/list"
##MODIFICACIONES PARA ENTREGABLES##
class EntregableList(ListView):
    model=Entregable
    template_name="AppCoder/entregable_list.html"
class EntregableDetalle(DetailView):
    model=Entregable
    template_name="AppCoder/entregable_detalle.html"
class EntregableCreacion(CreateView):
    model=Entregable
    success_url="/entregable/list"
    fields=['nombre','FechaDeEntrega','entregado']
class EntregableUpdate(UpdateView):
    model=Entregable
    success_url="/entregable/list"
    fields=['nombre','FechaDeEntrega','entregado']
class EntregableDelete(DeleteView):
    model=Entregable
    success_url="/entregable/list"
# Create your views here.
