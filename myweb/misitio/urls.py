from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes_list, name='clientes_list'),
    path('cliente/new', views.cliente_new, name='cliente_new'),
]



