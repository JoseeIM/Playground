from django import forms

class FormularioCurso(forms.Form):
    curso=forms.CharField(max_length=40)
    comision=forms.IntegerField()
class FormularioProfesor(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    email= forms.EmailField()
    profesion=forms.CharField(max_length=40)
class FormularioEstudiante(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    email= forms.EmailField()  
class FormularioEntregable(forms.Form):
    nombre=forms.CharField(max_length=40)
    FechaDeEntrega=forms.DateField()
    entregado=forms.BooleanField()