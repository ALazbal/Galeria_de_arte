from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dibujo(models.Model):

    galeria = (
        ("galeria","Galeria"),
        ("dibujo","Dibujos")
    )

    creador = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    galeria = models.CharField(max_length=15, choices=galeria, default='galeria')
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    dibujo = models.ImageField(upload_to="AppWeb/imagenes/",null=True, blank=True,)

class Comentario(models.Model):
    comentario = models.ForeignKey(Dibujo, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)