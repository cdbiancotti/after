from django.shortcuts import render
from inicio.forms import CrearGatoFormulario
from inicio.models import Gato

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_gato(request):
    mensaje = ''
    
    if request.method == 'POST':
        formulario = CrearGatoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            gato = Gato(nombre=info['nombre'],edad=info['edad'],fecha_nacimiento=info['fecha_nacimiento'])
            gato.save()
            mensaje = f'Se creo el gato {gato.nombre}'
        else:
            return render(request, 'inicio/crear_gato.html', {'formulario': formulario})
    
    formulario = CrearGatoFormulario()
    return render(request, 'inicio/crear_gato.html', {'formulario': formulario, 'mensaje': mensaje})
