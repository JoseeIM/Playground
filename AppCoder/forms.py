from django import forms
from django.forms.widgets import NumberInput,PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

CasosEntregado=[('True','Entregado'),('False','NoEntregado')]
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
    email=forms.EmailField()
class FormularioEntregable(forms.Form):
    nombre=forms.CharField(max_length=40)
    Fecha_De_Entrega=forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    entregado=forms.ChoiceField(widget=forms.RadioSelect, choices=CasosEntregado)

class SignUpForm (UserCreationForm):
    class Meta:
        model = User 
        fields=[
            'username',
            'email',
            'password1',
            'password2'
        ]

class UserEditForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password1',
            'password2',
        ]
        help_texts={k:""for k in fields}
class FormularioDudas(forms.Form):
    asunto=forms.CharField(max_length=40)
    materia=forms.CharField(max_length=40)
    desarrollo=forms.CharField(max_length=1000,widget=forms.Textarea)
