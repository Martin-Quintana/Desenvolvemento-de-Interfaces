import os, var, conexion

import reportlab
from PyQt6 import QtSql
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
            items = ['DNI', 'Nombre', 'Direccion', 'Municipio', 'Provincia']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.line(50, 680, 525, 680)
            var.report.drawString(60, 670, str(items[0]))
            var.report.drawString(120, 670, str(items[1]))
            var.report.drawString(225, 670, str(items[2]))
            var.report.drawString(345, 670, str(items[3]))
            var.report.drawString(460, 670, str(items[4]))
            var.report.line(50, 667, 525, 667)

            query = QtSql.QSqlQuery()
            query.prepare('select dni, nombre, direccion, municipio, provincia from clientes order by nombre')
            var.report.setFont('Helvetica', size=8)

            if query.exec():
                i = 55
                j = 650
                while query.next():
                    if j <= 80:
                        var.report.drawString(460, 90, 'Pagina siguiente...')
                        var.report.showPage()
                        Informes.cabecera(titulo)
                        Informes.pieInforme(titulo)
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.line(50, 680, 525, 680)
                        var.report.drawString(60, 670, str(items[0]))
                        var.report.drawString(120, 670, str(items[1]))
                        var.report.drawString(225, 670, str(items[2]))
                        var.report.drawString(345, 670, str(items[3]))
                        var.report.drawString(460, 670, str(items[4]))
                        var.report.line(50, 667, 525, 667)
                        i = 60
                        j = 700
                    dni = str(query.value(0))
                    dniCensored = '*****' + dni[5] + dni[6] + dni[7] + '*'
                    var.report.setFont('Helvetica', size=8)
                    var.report.drawString(i, j, dniCensored)
                    var.report.drawString(i + 65, j, str(query.value(1)))
                    var.report.drawString(i + 170, j, str(query.value(2)))
                    var.report.drawString(i + 290, j, str(query.value(3)))
                    var.report.drawString(i + 405, j, str(query.value(4)))
                    j = j - 20

            var.report.save()


            fecha = datetime.today()
            fecha = fecha.strftime('%Y-%m-%d-%H.%M.%S')
            copia = (str(fecha) + '_Clientes.pdf')
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Copia',
                                                                copia, '.pdf')
            # Creamos la Backup
            if var.dlgabrir.accept and filename != '':
                os.write(os.open('informes/listadoClientes.pdf', os.O_RDWR), str.encode(copia))

            '''
            for file in os.listdir(rootPath):
                if file.endswith('Clientes.pdf'):
                    os.startfile('%s\%s' % (rootPath, file))
            '''
        except Exception as error:
            print('Error informes estado de clientes', error)

    def listAutos(self):

        try:
            var.report = canvas.Canvas('informes/listadoAutos.pdf')
            titulo = 'LISTADO VEHICULO'
            var.report.drawString(250, 685, titulo)
            Informes.pieInforme(titulo)
            Informes.cabecera(titulo)
            items = ['Matricula', 'DNI', 'Marca', 'Modelo', 'Motor']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.line(50, 680, 525, 680)
            var.report.drawString(60, 670, str(items[0]))
            var.report.drawString(120, 670, str(items[1]))
            var.report.drawString(225, 670, str(items[2]))
            var.report.drawString(345, 670, str(items[3]))
            var.report.drawString(460, 670, str(items[4]))
            var.report.line(50, 667, 525, 667)

            query = QtSql.QSqlQuery()
            query.prepare('select matricula, dnicli, marca, modelo, motor from coches order by marca, modelo')
            var.report.setFont('Helvetica', size=8)

            if query.exec():
                i = 55
                j = 650
                while query.next():
                    if j <= 80:
                        var.report.drawString(460, 90, 'Pagina siguiente...')
                        var.report.showPage()
                        Informes.cabecera(titulo)
                        Informes.pieInforme(titulo)
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.line(50, 680, 525, 680)
                        var.report.drawString(60, 680, str(items[0]))
                        var.report.drawString(100, 680, str(items[1]))
                        var.report.drawString(300, 680, str(items[2]))
                        var.report.drawString(300, 680, str(items[3]))
                        var.report.drawString(460, 680, str(items[4]))
                        var.report.line(50, 667, 525, 667)
                        i = 60
                        j = 700

                    dni = str(query.value(1))
                    dniCensored = '*****' + dni[5] + dni[6] + dni[7] + '*'

                    var.report.setFont('Helvetica', size=8)
                    var.report.drawString(i, j, str(query.value(0)))
                    var.report.drawString(i + 65, j, dniCensored)
                    var.report.drawString(i + 170, j, str(query.value(2)))
                    var.report.drawString(i + 290, j, str(query.value(3)))
                    var.report.drawString(i + 405, j, str(query.value(4)))
                    j = j - 20
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
            var.report.setFont('Helvetica', size=10)
            var.report.line(50, 815, 525, 815)
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
            var.report.drawImage(logo, 400, 725, width=150, height=70)


        except Exception as error:
            print('Error en la cabecera clase Informes ', error)
