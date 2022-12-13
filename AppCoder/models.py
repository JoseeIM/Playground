from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    comision=models.IntegerField()
    def __str__(self):
        return f"Nombre:{self.nombre} - Comision:{self.comision}"
class Estudiante(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email= models.EmailField()
    def __str__(self):
        return f"Nombre:{self.nombre} - Apellido:{self.apellido}"  
class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email= models.EmailField()
    profesion=models.CharField(max_length=40)
    def __str__(self):
        return f"Nombre:{self.nombre} - Apellido:{self.apellido}"
class Entregable(models.Model):
    nombre=models.CharField(max_length=40)
    FechaDeEntrega=models.DateField()
    entregado=models.BooleanField()
    def __str__(self):
        return f"Nombre:{self.nombre} - Fecha de Entrega:{self.FechaDeEntrega}"
class Avatar(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares',null=True,blank=True)
class Duda(models.Model):
    asunto=models.CharField(max_length=40,default="nada")
    materia=models.CharField(max_length=40,default="nada")
    desarrollo=models.CharField(max_length=1000,default="nada")
    def __str__(self):
        return f"Asunto:{self.asunto} - Materia:{self.materia}"
