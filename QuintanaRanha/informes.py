import os, var
from reportlab import *
from datetime import datetime

from reportlab.pdfgen import canvas


class Informes:

    def listClientes(self):

        try:
            var.report = canvas.Canvas('informes/listadoClientes.pdf')
            titulo = 'LISTADO CLIENTES'
            var.report.drawString(100, 750, titulo)

            var.report.save()
            Informes.pieInforme(titulo)
            rootPath = '.\\informes'

            for file in os.listdir(rootPath):
                if file.endswith('Clientes.pdf'):
                    os.startfile('%s\%s' % (rootPath, file))
        except Exception as error:
            print('Error informes estado de clientes' , error)

    def listAutos(self):

        try:
            var.report = canvas.Canvas('informes/listadoAutos.pdf')
            titulo = 'LISTADO VEHICULO'
            var.report.drawString(100, 750, titulo)
            var.report.save()
            Informes.pieInforme(titulo)
            rootPath = '.\\informes'

            for file in os.listdir(rootPath):
                if file.endswith('Autos.pdf'):
                    os.startfile('%s\%s' % (rootPath, file))
        except Exception as error:
            print('Error informes estado de vehiculos' , error)

    def pieInforme(titulo):

        try:
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%Y-%m-%d-%H.%M.%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(460, 40, str('Pagina %s' % var.report.getPageNumber()))
        except Exception as error:
            print('Error pie informe de cualquier tipo ' , error)
