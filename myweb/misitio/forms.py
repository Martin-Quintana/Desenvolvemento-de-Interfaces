from django import forms
from .models import Cliente
from .models import Productos

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [ 'dni', 'nombre', 'fecha_alta', 'direccion', 'mobile' ]

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['producto', 'descripcion', 'precio']
