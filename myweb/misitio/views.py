from django.shortcuts import render, redirect
from .models import Cliente, Productos
from django.utils import timezone
from .forms import ClienteForm
from .forms import ProductosForm
from django.views.generic import CreateView


# Create your views here.

def clientes_list(request):
    clientes = Cliente.objects.order_by('fecha_alta')
    return  render(request, 'misitio/clientes_list.html', {'clientes': clientes})

def cliente_new(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('clientes_list')
    else:
        form = ClienteForm()

    return render(request, 'misitio/clientes_edit.html', {'form': form})

def productos_list(request):
    productos = Productos.objects.order_by('precio')
    return  render(request, 'misitio/productos_list.html', {'productos': productos})

def producto_new(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('productos_list')
    else:
        form = ProductosForm()
    return render(request, 'misitio/productos_edit.html', {'form': form})

def index(request):
    return render(request, 'misitio/index.html')