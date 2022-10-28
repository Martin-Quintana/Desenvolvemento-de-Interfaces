from django.shortcuts import render

# Create your views here.
def clientes_list (resquest):
    return render(resquest, 'misitio/clientes_list.html', {})