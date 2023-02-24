from django.urls import path
from AppWeb.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [ 

    path("", inicio, name="Inicio"),
    path("acercaDeMi/", acercaDeMi, name="about"),
    path("galeria/", galeria, name="Galeria"),
    path("comentarios/", ComentarioPagina.as_view(), name="Comentarios"),
    path("ver_comentarios/", ver_comentarios, name="Ver Comentarios"),
    path("ver_dibujos/", ver_dibujos, name="Ver Dibujos"),


    #dibujos
    path("dibujo_uno/", dibujoUno, name="dibujo_uno"),
    path("dibujo_dos/", dibujoDos, name="dibujo_dos"),
    path("dibujo_tres/", dibujoTres, name="dibujo_tres"),
    path("dibujo_cuatro/", dibujoCuatro, name="dibujo_cuatro"),
    path("dibujo_cinco/", dibujoCinco, name="dibujo_cinco"),
    path("dibujo_seis/", dibujoSeis, name="dibujo_seis"),

    
    path("agregar_dibujo/", AgregarDibujo.as_view(), name="nuevo"),


    #login - register- logout
    path("login/", inicioSesion, name="Login" ),
    path("registrar/", registro, name="Registro"),
    path("cerrar_sesion/", LogoutView.as_view(template_name="AppWeb/logout.html"), name="Cerrar Sesion"),

    #editar perfiles
    path("editar/", editarUsuario, name="Editar Usuario"),

]   