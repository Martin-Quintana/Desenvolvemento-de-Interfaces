import os, var
from reportlab import *
from datetime import datetime

from reportlab.pdfgen import canvas


class Informes:

    def listClientes(self):

        try:
            var.report = canvas.Canvas('informes/listadoClientes.pdf')
            titulo = 'LISTADO CLIENTES'
            var.report.drawString(250, 685, titulo)
            Informes.pieInforme(titulo)
            Informes.cabecera(titulo)
            var.report.save()
            rootPath = '.\\informes'

            for file in os.listdir(rootPath):
                if file.endswith('Clientes.pdf'):
                    os.startfile('%s\%s' % (rootPath, file))
        except Exception as error:
            print('Error informes estado de clientes', error)

    def listAutos(self):

        try:
            var.report = canvas.Canvas('informes/listadoAutos.pdf')
            titulo = 'LISTADO VEHICULO'
            var.report.drawString(250, 685, titulo)
            Informes.pieInforme(titulo)
            Informes.cabecera(titulo)
            var.report.save()
            rootPath = '.\\informes'

            for file in os.listdir(rootPath):
                if file.endswith('Autos.pdf'):
                    os.startfile('%s\%s' % (rootPath, file))
        except Exception as error:
            print('Error informes estado de vehiculos', error)

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
            print('Error pie informe de cualquier tipo ', error)

    def cabecera(titulo):
        try:
            logo = '.\img\logo.png'
            var.report.line(50, 800, 525, 800)
            var.report.setFont('Helvetica', size=10)

            var.report.setAuthor('Martin Quintana')

            textCIF = 'A0000000H'
            textnom = 'TALLER MECANICO TEIS'
            textdir = 'Avenida de Galicia, 101'
            textpost = 'Vigo - 36216 - España'
            textemail = 'iesteis@iesteis.es'
            texttlfo = 'Telefono: 886 12 04 64'
            var.report.drawString(50, 805, textCIF)
            var.report.drawString(50, 785, textnom)
            var.report.drawString(50, 765, textdir)
            var.report.drawString(50, 750, textpost)
            var.report.drawString(50, 735, texttlfo)
            var.report.drawString(50, 720, textemail)
            var.report.drawImage(logo, 400, 725, width=150, height= 70)
            var.report.line(50, 710, 525, 710)




        except Exception as error:
            print('Error en la cabecera clase Informes ', error)
