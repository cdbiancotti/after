from django.shortcuts import render
from inicio.forms import CrearGatoFormulario, BusquedaGatoFormulario
from inicio.models import Gato

from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy


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

def listar_gatos(request):
    
    formulario = BusquedaGatoFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre', '')
        lista_gatos = Gato.objects.filter(nombre__icontains=nombre_a_buscar)
    
    formulario = BusquedaGatoFormulario()
    return render(request, 'inicio/gatos.html', {'formulario': formulario, 'lista_gatos': lista_gatos})


class DetalleGato(DetailView):
    model = Gato
    template_name = "inicio/detalle_gato.html"


class ModificarGato(UpdateView):
    model = Gato
    fields = ['nombre', 'edad', 'fecha_nacimiento']
    template_name = "inicio/modificar_gato.html"
    success_url = reverse_lazy('inicio:gatos')


class EliminarGato(DeleteView):
    model = Gato
    template_name = "inicio/eliminar_gato.html"
    success_url = reverse_lazy('inicio:gatos')
