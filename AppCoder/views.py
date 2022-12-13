from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso,Profesor,Estudiante,Entregable,Avatar,Duda
from AppCoder.forms import FormularioCurso,FormularioProfesor,FormularioEntregable,FormularioEstudiante,SignUpForm,UserEditForm,FormularioDudas
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
def inicio(request):
    return render (request,"AppCoder/incio.html")

def cursos(request):
    return render (request,"AppCoder/cursos.html")
@login_required
def estudiantes(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    return render (request,"AppCoder/estudiantes.html",{"url":avatares[0].imagen.url})
@login_required
def profesores(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    return render (request,"AppCoder/profesor.html",{"url":avatares[0].imagen.url})
@login_required
def entregables(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    return render (request,"AppCoder/entregables.html",{"url":avatares[0].imagen.url})
@login_required
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
    avatares=Avatar.objects.filter(user=request.user.id)
    return render (request,"AppCoder/CursosCreacion.html",{"miFormulario":miFormulario,"url":avatares[0].imagen.url})
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
    avatares=Avatar.objects.filter(user=request.user.id)
    return render (request,"AppCoder/ProfesorCreacion.html",{"miFormulario":miFormulario,"url":avatares[0].imagen.url})
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
    avatares=Avatar.objects.filter(user=request.user.id)
    return render (request,"AppCoder/EstudiantesCreacion.html",{"miFormulario":miFormulario,"url":avatares[0].imagen.url})
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
    avatares=Avatar.objects.filter(user=request.user.id)
    return render (request,"AppCoder/EntregablesCreacion.html",{"miFormulario":miFormulario,"url":avatares[0].imagen.url})
@login_required
def BuscadorCurso(request):#BusquedaDeCursos
    if request.GET.get('comision', False):
        comision=request.GET['comision']
        cursos=Curso.objects.filter(comision__icontains=comision)
        return render(request,"AppCoder/CursosBuscador.html",{"cursos":cursos,"comision":comision})
    else:
        respuesta="No enviaste datos"
    avatares=Avatar.objects.filter(user=request.user.id)
    return render(request,"AppCoder/CursosBuscador.html",{"respuesta":respuesta,"url":avatares[0].imagen.url})
def BuscadorEstudiantes(request):#BusquedaDeEstudiantes
    if request.GET.get('apellido', False):
        apellido=request.GET['apellido']
        estudiantes=Estudiante.objects.filter(apellido__icontains=apellido)
        return render(request,"AppCoder/EstudiantesBuscador.html",{"estudiantes":estudiantes,"apellido":apellido})
    else:
        respuesta="No enviaste datos"
    avatares=Avatar.objects.filter(user=request.user.id)
    return render(request,"AppCoder/EstudiantesBuscador.html",{"respuesta":respuesta,"url":avatares[0].imagen.url})
def BuscadorProfesor(request):#BusquedaDeProfesorS
    if request.GET.get('apellido', False):
        apellido=request.GET['apellido']
        profesores=Profesor.objects.filter(apellido__icontains=apellido)
        return render(request,"AppCoder/ProfesorBuscador.html",{"profesores":profesores,"apellido":apellido})
    else:
        respuesta="No enviaste datos"
    avatares=Avatar.objects.filter(user=request.user.id)
    return render(request,"AppCoder/ProfesorBuscador.html",{"respuesta":respuesta,"url":avatares[0].imagen.url})
def BuscadorEntregables(request):#BusquedaDeEntregables
    if request.GET.get('nombre', False):
        nombre=request.GET['nombre']
        entregables=Entregable.objects.filter(nombre__icontains=nombre)
        return render(request,"AppCoder/EntregablesBuscador.html",{"entregables":entregables,"nombre":nombre})
    else:
        respuesta="No enviaste datos"
    avatares=Avatar.objects.filter(user=request.user.id)
    return render(request,"AppCoder/EntregablesBuscador.html",{"respuesta":respuesta,"url":avatares[0].imagen.url})
##MODIFICACIONES PARA EL CURSO##
class CursoList(ListView):
    model=Curso
    template_name="AppCoder/curso_list.html"
class CursoDetalle(LoginRequiredMixin,DetailView):
    model=Curso
    template_name="AppCoder/curso_detalle.html"
class CursoCreacion(LoginRequiredMixin,CreateView):
    model=Curso
    success_url="/curso/list"
    fields=['nombre','comision']
class CursoUpdate(LoginRequiredMixin,UpdateView):
    model=Curso
    success_url="/curso/list"
    fields=['nombre','comision']
class CursoDelete(LoginRequiredMixin,DeleteView):
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
##Login y Register##
class SingUpView(CreateView):
    form_class= SignUpForm
    success_url=reverse_lazy('Inicio')
    template_name='AppCoder/registro.html'
class AdminLoginView(LoginView):
    template_name='AppCoder/login.html'
class AdminLogoutView(LogoutView):
    template_name='AppCoder/inicio.html'
##EDICION DE PERFILES
@login_required
def VerPerfil(request):
    usuario=request.user
    if request.method=='GET':
            nombre = usuario.username
            email= usuario.email 
    avatares=Avatar.objects.filter(user=request.user.id)
    return render (request,"AppCoder/VerPerfil.html",{"email":email,"usuario":usuario,"url":avatares[0].imagen.url})
@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method=='POST':
        usuario_form=UserEditForm(request.POST)
        if usuario_form.is_valid:
            informacion=usuario_form.cleaned_data
            usuario.username = informacion['username']
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()  
            return render (request,"AppCoder/inicio.html")
    else:
        usuario_form=UserEditForm(initial={'username':usuario.username, 'email':usuario.email})
    avatares=Avatar.objects.filter(user=request.user.id)
    return render (request,"AppCoder/editarPerfil.html",{"form":usuario_form,"usuario":usuario,"url":avatares[0].imagen.url})
@login_required
def inicio(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    return render (request,"AppCoder/inicio.html",{"url":avatares[0].imagen.url})
@login_required
def cursos(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    return render (request,"AppCoder/cursos.html",{"url":avatares[0].imagen.url})
@login_required
def dudas(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    return render (request,"AppCoder/dudas.html",{"url":avatares[0].imagen.url})
@login_required
def CreacionDudas(request):##FormularioDuda
    if request.method == 'POST':
        miFormulario= FormularioDudas(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            dudas= Duda (asunto=informacion['asunto'], materia=informacion['materia'],desarrollo=informacion['desarrollo'] )
            dudas.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario=FormularioDudas()
    avatares=Avatar.objects.filter(user=request.user.id)
    return render (request,"AppCoder/DudaCreacion.html",{"miFormulario":miFormulario,"url":avatares[0].imagen.url})
class DudaList(ListView):
    model=Duda
    template_name="AppCoder/duda_list.html"
class DudaDetalle(DetailView):
    model=Duda
    template_name="AppCoder/duda_detalle.html"
class DudaUpdate(UpdateView):
    model=Duda
    success_url="/dudas/list"
    fields=['asunto','materia','desarrollo']
class DudaDelete(DeleteView):
    model=Duda
    success_url="/dudas/list"
# Create your views here.