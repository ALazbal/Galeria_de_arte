from django.shortcuts import render
from django.http import HttpResponse
from AppWeb.models import * 
from AppWeb.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


@login_required(login_url= "Login")
def inicio(request):

    return render(request, "AppWeb/inicio.html")


def acercaDeMi(request):

    return render(request, "AppWeb/acercaDeMi.html")

@login_required(login_url= "Login")
def galeria(request):

   return render(request, "AppWeb/galeria.html")
   

    
#-------------- GALERIA ----------------------------

def dibujoUno(request):

    return render(request, "AppWeb/dibujo1.html")

def dibujoDos(request):

    return render(request, "AppWeb/dibujo2.html")

def dibujoTres(request):

    return render(request, "AppWeb/dibujo3.html")

def dibujoCuatro(request):

    return render(request, "AppWeb/dibujo4.html")

def dibujoCinco(request):

    return render(request, "AppWeb/dibujo5.html")

def dibujoSeis(request):

    return render(request, "AppWeb/dibujo6.html")

#------------ LOGIN - REGISTRO - LOGOUT --------------------------

def inicioSesion(request):

    if request.method == 'POST':
        
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  

            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contra)

            if user:
                
                login(request, user)

                return render(request, "AppWeb/inicio.html", {"mensaje":f"Sesion iniciada, bienvenido/a {usuario}"})
            
        else:
                
            return render(request, "AppWeb/inicio.html", {"mensaje":"Datos incorrectos, reintentar."})
                                                        
    else:

        form = AuthenticationForm()

    return render(request, "AppWeb/login.html", {"formulario": form})


def registro(request):

      if request.method == 'POST':

            form = UsuarioRegistro(request.POST)
          
            if form.is_valid():

                  username = form.cleaned_data['username']
                  
                  form.save()
                  
                  return render(request,"AppWeb/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            form = UsuarioRegistro()       
               

      return render(request,"AppWeb/registro.html" ,  {"formulario":form})


#----------------- EDITAR USUARIO-------------------------------


@login_required
def editarUsuario(request):

    usuario = request.user

    if request.method == "POST" :

        form = FormularioEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password = (info["password1"])
            usuario.first_name = (info["first_name"])
            usuario.last_name = (info["last_name"])

            usuario.save()

            return render(request, "AppWeb/inicio.html")
    else :
                          
        form = FormularioEditar(initial = {

            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name": usuario.last_name
        })

    return render(request, "AppWeb/editarPerfil.html", {"formulario":form, "usuario":usuario})



#------------- AGREGAR DIBUJO -------------------

class AgregarDibujo(LoginRequiredMixin, CreateView):
    
    model = Dibujo
    form_class = FormularioNuevoDibujo
    success_url = reverse_lazy("Ver Dibujos")
    template_name = "AppWeb/agregarDibujo.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AgregarDibujo, self).form_valid(form)

@login_required(login_url= "Login")
def ver_dibujos(request):

    listaDibujos = Dibujo.objects.all()

    return render(request, "AppWeb/verDibujos.html", {"listaDibujos":listaDibujos})


#------------- COMENTARIOS -------------------------

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'AppWeb/comentarios.html'
    success_url = reverse_lazy('Ver Comentarios')

@login_required(login_url= "Login")
def ver_comentarios(request):

    listaComentarios = Comentario.objects.all()

    return render(request, "AppWeb/verComentarios.html", {"listaComentarios":listaComentarios})

