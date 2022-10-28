from django.shortcuts import render
from .models import Cliente
from django.utils import timezone
# Create your views here.

def clientes_list(request):
    clientes = Cliente.objects.order_by('fecha_alta')
    return  render(request, 'misitio/clientes_list.html', {'clientes': clientes})