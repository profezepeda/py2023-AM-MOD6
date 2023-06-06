from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def saludo(request):
    return render(request, "saludo.html")

def saludo2(request):
    persona = {
        "nombre": "Juan",
        "apellido": "Perez",
        "edad": 30,
        "hobbies": ["Futbol", "Programacion", "Videojuegos"]
    }
    return render(request, "saludo2.html", { "persona": persona })

class saludoClase(TemplateView):
    template_name = "saludo.html"

    def get(self, request, *args, **kwargs):
        persona = {
            "nombre": "Juan",
            "apellido": "Perez",
            "edad": 30,
            "hobbies": ["Futbol", "Programacion", "Videojuegos"]
        }
        return render(request, self.template_name, { "persona": persona })