from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppWeb.models import *


#----------- USUARIO ----------------------

class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget = forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class FormularioEditar(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar Contraseña", widget = forms.PasswordInput)

    class Meta:

        model = User
        fields = ["first_name", "last_name", "password1", "password2"]  

#------------------------------------------------------

class FormularioNuevoDibujo(forms.ModelForm):
    
    class Meta:
        model = Dibujo
        fields = ('creador', 'descripcion', 'dibujo')

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'galeria' : forms.Select(attrs={'class': 'form-control'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'emailContacto' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class FormularioComentario(forms.ModelForm):
    
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }
