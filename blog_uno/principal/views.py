from typing import Any, Dict
import uuid
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from principal.forms import FormularioContactoForm
from principal.models import FormularioContacto

# Create your views here.

categorias = [
  {
    'idcategoria': 1,
    'nombre': 'Tecnologia',
  },
  {
    'idcategoria': 2,
    'nombre': 'Deportes',
  },
  {
    'idcategoria': 3,
    'nombre': 'Python',
  },
  {
    'idcategoria': 4,
    'nombre': 'Django',
  },
]

def home(request):
  if request.method == 'GET':
    pass
  if request.method == 'POST':
    pass
  return render(request, 'principal/home.html')

class HomeView(TemplateView):
  template_name = 'principal/home_part.html'

  def get(self, request, *args, **kwargs):
    titulo = "NOTICIAS DESTACADAS"
    noticias = [
      {
        'idnoticia': str(uuid.uuid4()),
        'titulo': 'Primera Noticia',
        'contenido': 'Contenido de la noticia 1',
        'imagen': 'https://picsum.photos/900/100?1'
      },
      {
        'idnoticia': str(uuid.uuid4()),
        'titulo': 'Segunda Noticia',
        'contenido': 'Contenido de la noticia 2',
        'imagen': 'https://picsum.photos/900/100?2'
      },
      {
        'idnoticia': str(uuid.uuid4()),
        'titulo': 'Tercera Noticia',
        'contenido': 'Contenido de la noticia 3',
        'imagen': 'https://picsum.photos/900/100?3'
      },
      {
        'idnoticia': str(uuid.uuid4()),
        'titulo': 'Cuarta Noticia',
        'contenido': 'Contenido de la noticia 4',
        'imagen': 'https://picsum.photos/900/100?4'
      },
      {
        'idnoticia': str(uuid.uuid4()),
        'titulo': 'quinta noticia',
        'contenido': 'Contenido de la noticia 5',
        'imagen': 'https://picsum.photos/900/100?4'
      }
    ]
    contexto = {
      'titulo': titulo, 
      'noticias': noticias, 
      "categorias": categorias
    }
    return render(request, self.template_name, contexto)

  def post(self, request, *args, **kwargs):
    return render(request, self.template_name)
  
class CategoriaView(TemplateView):
  template_name = 'principal/categoria_part.html'
  
  def get(self, request, idcategoria, *args, **kwargs):
    titulo = None
    for categoria in categorias:
      if categoria['idcategoria'] == idcategoria:
        titulo = categoria['nombre']
        break
    contexto = {
      'idcategoria': idcategoria,
      'titulo': titulo,
      'noticias': [],
      "categorias": categorias
    }
    if titulo is None:
      return redirect('home')
    return render(request, self.template_name, contexto)

class ContactoView(TemplateView):
  template_name = 'principal/contacto_part.html'
  
  def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context["info"] = "Información complementaria"
    return context

  def get(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    context["formulario"] = FormularioContactoForm()
    return render(request, self.template_name, context)

  def post(self, request, *args, **kwargs):
    form = FormularioContactoForm(request.POST)
    mensajes = {
      "enviado": False,
      "resultado": None
    }
    if form.is_valid():
      nombre = form.cleaned_data['nombre']
      telefono = form.cleaned_data['telefono']
      email = form.cleaned_data['email']
      mensaje = form.cleaned_data['mensaje']

      registro = FormularioContacto(
        nombre=nombre,
        telefono=telefono,
        email=email,
        mensaje=mensaje
      )
      registro.save()

      mensajes = { "enviado": True, "resultado": "Mensaje enviado correctamente" }
    else:
      mensajes = { "enviado": False, "resultado": form.errors }
    return render(request, self.template_name, { "formulario": form, "mensajes": mensajes})