from django import forms

class CrearGatoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(required=False, widget=forms.DateInput(format='%d/%m/%Y'), input_formats=('%d/%m/%Y', ))
    
    
class BusquedaGatoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)