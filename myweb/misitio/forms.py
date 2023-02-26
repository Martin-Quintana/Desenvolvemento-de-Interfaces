from django import forms
from .models import Cliente
from .models import Productos


# Create the form class.
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['dni', 'nombre', 'fecha_alta', 'direccion', 'mobile']
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'DNI del cliente',
                                            'required': True,
                                            'autofocus': True, }),
            'nombre': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Nombre del cliente',
                                             'required': True,
                                             'autofocus': True}),
            'fecha_alta': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Fecha de alta del cliente',
                                                 'required': True,
                                                 'autofocus': True}),
            'direccion': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Dirección del cliente',
                                                'required': True,
                                                'autofocus': True}),
            'mobile': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Teléfono del cliente',
                                             'required': True,
                                             'autofocus': True})
        }



class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['producto', 'descripcion', 'precio']
        widgets = {
            'producto': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Nombre del producto',
                                               'required': True,
                                               'autofocus': True, }),
            'descripcion': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Descripción del producto',
                                                  'required': True,
                                                  'autofocus': True, }),
            'precio': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Precio del producto',
                                             'required': True,
                                             'autofocus': True, }),
        }
