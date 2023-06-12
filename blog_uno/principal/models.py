from django.db import models

# Create your models here.

class FormularioContacto(models.Model):
  nombre = models.CharField(max_length=50, null=False, blank=False)
  email = models.EmailField(max_length=150, null=False, blank=False)
  telefono = models.CharField(max_length=15, null=False, blank=False)
  mensaje = models.CharField(max_length=1000, null=False, blank=False)

  def __str__(self):
    return self.nombre
  
  class Meta:
    permissions = [
      ('puede_leer_formulario', 'Permiso para lectura de formularios')
    ]