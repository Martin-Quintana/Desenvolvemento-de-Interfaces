import datetime
from django.template import Template, Context

from django.http import HttpResponse


def saludo(request):  # primera vista

    nombre = "Juan"

    doc_externo = open('C:\Users\marti\Documents\ClaseCS2DAM\Desenvolvemento-de-Interfaces\ProyectosDjango\myweb\myweb\plantillas\miplantilla.html')
    plt = Template(doc_externo.read())

    doc_externo.close()
    ctx = Context({"nomnre_persona": nombre, "momento_actual": datetime.datetime.now()})

    documento = plt.render(ctx)

    return HttpResponse(documento)


def despedida(request):
    return HttpResponse("Adios mundo")

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = "<html><body><h1>Fecha y hora actuales %s</h1></body></html>" % fecha_actual
    return HttpResponse(documento)

def calculaEdad(request, edad, agno):
    edadActual = 18
    periodo = agno - 2022
    edadFutura = edad + periodo
    documento = "<html><body><h1>En el año %s tendrás %s años</h1></body></html>" % (agno, edadFutura)
    return HttpResponse(documento)