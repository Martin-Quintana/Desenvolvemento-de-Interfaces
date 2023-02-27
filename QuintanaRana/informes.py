import os, var
from PyQt6 import QtSql, QtWidgets
from reportlab.pdfgen import canvas
from datetime import datetime

import conexion


class Informes:
    def listClientes(self):
        try:
            var.report = canvas.Canvas('informes/listadoClientes.pdf')
            titulo = 'LISTADO CLIENTES'
            Informes.pieInforme(titulo)
            Informes.topInforme(titulo)

            items = ['DNI', 'Nombre', 'Direccion', 'Municipio', 'Provincia']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(70, 692, str(items[0]))
            var.report.drawString(140, 692, str(items[1]))
            var.report.drawString(250, 692, str(items[2]))
            var.report.drawString(355, 692, str(items[3]))
            var.report.drawString(455, 692, str(items[4]))
            var.report.line(50, 680, 525, 680)

            query = QtSql.QSqlQuery()
            query.prepare('select dni, nombre, direccion, municipio, provincia from clientes order by nombre')
            var.report.setFont('Helvetica', size=8)

            if query.exec():
                i = 55
                j = 660
                while query.next():
                    if j <= 80:
                        var.report.drawString(460, 90, 'Página siquiente... ')
                        var.report.showPage()
                        Informes.topInforme(titulo)
                        Informes.pieInforme(titulo)
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(70, 692, str(items[0]))
                        var.report.drawString(140, 692, str(items[1]))
                        var.report.drawString(250, 692, str(items[2]))
                        var.report.drawString(355, 692, str(items[3]))
                        var.report.drawString(455, 692, str(items[4]))
                        var.report.line(50, 680, 525, 680)
                        i = 55
                        j = 660
                    var.report.setFont('Helvetica', size=8)

                    dni = str(query.value(0))
                    dniCensored = '*****' + dni[5] + dni[6] + dni[7] + '*'
                    var.report.drawString(i + 5, j, dniCensored)
                    var.report.drawString(i + 80, j, str(query.value(1)))
                    var.report.drawString(i + 185, j, str(query.value(2)))
                    var.report.drawString(i + 303, j, str(query.value(3)))
                    var.report.drawString(i + 403, j, str(query.value(4)))
                    j = j - 20

            var.report.save()
            rootPath = '.\\informes'

            file = ('Informe Clientes.pdf')

            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Datos', file, '.pdf')
            #wb = pdf.Workbook()
            #wb.save(directorio)

            #for file in os.listdir(rootPath):
            #    if file.endswith('Clientes.pdf'):
            #        os.startfile('%s\%s' % (rootPath, file))
        except Exception as error:
            print('Error informes estado cliente', error)

    def listAutos(self):
        try:
            var.report = canvas.Canvas('informes/listadoAutos.pdf')
            titulo = 'LISTADO VEHICULOS'
            Informes.pieInforme(titulo)
            Informes.topInforme(titulo)

            items = ['Matricula', 'DNI', 'Marca', 'Modelo', 'Motor']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(55, 692, str(items[0]))
            var.report.drawString(147, 692, str(items[1]))
            var.report.drawString(240, 692, str(items[2]))
            var.report.drawString(355, 692, str(items[3]))
            var.report.drawString(455, 692, str(items[4]))
            var.report.line(50, 680, 525, 680)

            query = QtSql.QSqlQuery()
            query.prepare('select matricula, dnicli, marca, modelo, motor from coches')
            var.report.setFont('Helvetica', size=8)

            if query.exec():
                i = 55
                j = 660
                while query.next():
                    if j <= 80:
                        var.report.drawString(460, 90, 'Página siquiente... ')
                        var.report.showPage()
                        Informes.topInforme(titulo)
                        Informes.pieInforme(titulo)
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(55, 692, str(items[0]))
                        var.report.drawString(147, 692, str(items[1]))
                        var.report.drawString(240, 692, str(items[2]))
                        var.report.drawString(355, 692, str(items[3]))
                        var.report.drawString(455, 692, str(items[4]))
                        var.report.line(50, 680, 525, 680)
                        i = 55
                        j = 660
                    var.report.setFont('Helvetica', size=8)

                    dni = str(query.value(1))
                    dniCensored = '*****' + dni[5] + dni[6] + dni[7] + '*'

                    var.report.drawString(i + 5, j, str(query.value(0)))
                    var.report.drawString(i + 80, j, dniCensored)
                    var.report.drawString(i + 185, j, str(query.value(2)))
                    var.report.drawString(i + 303, j, str(query.value(3)))
                    var.report.drawString(i + 403, j, str(query.value(4)))
                    j = j - 20

            var.report.save()
            rootPath = '.\\informes'
            for file in os.listdir(rootPath):
                if file.endswith('Autos.pdf'):
                    os.startfile('%s\%s' % (rootPath, file))
        except Exception as error:
            print('Error informes estado vehiculos', error)

    def topInforme(titulo):
        try:
            logo = '.\img\logo-taller.png'
            var.report.line(50, 800, 525, 800)
            var.report.setFont('Helvetica-Bold', size=14)
            var.report.drawString(55, 785, 'Taller Mecanico Teis')
            var.report.drawString(230, 720, titulo)
            var.report.line(50, 710, 525, 710)
            var.report.drawImage(logo, 440, 733, width=80, height=45)
            var.report.setFont('Helvetica', size=9)
            var.report.drawString(55, 770, 'CIF: A12345678')
            var.report.drawString(55, 760, 'Avda. Galicia 101')
            var.report.drawString(55, 750, 'Teis, Vigo 36216')
            var.report.drawString(55, 740, 'Tlf: 986 123 456')
            var.report.drawString(55, 730, 'Email: mitaller@hotmail.com')
        except Exception as error:
            print("Error en cabecera de informe", error)

    def pieInforme(titulo):
        try:
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 35, str(fecha))
            var.report.drawString(250, 35, str(titulo))
            var.report.drawString(493, 35, str('Pagina %s' % var.report.getPageNumber()))

        except Exception as error:
            print('Error en pie informes estado cliente', error)

    def factura(self):
        try:
            var.report = canvas.Canvas('Informes/factura.pdf')
            titulo = 'FACTURA'
            Informes.pieInforme(titulo)
            Informes.topInforme(titulo)
            cliente = []
            dni = str(var.ui.lblDnifac.text())
            nfac = str(var.ui.lblNumfac.text())
            fechafac = str(var.ui.lblFechafac.txt())
            if nfac == '':
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('Debe seleccionar una factura')
                msg.exec()
            else:
                cliente = conexion.Conexion.oneCli(dni)
                var.report.setFont('Helvetica-Bold', size=9)
                var.report.drawString(55, 680, 'DATOS CLIENTE')
                var.report.drawString(400, 660, 'N Factura: ')
                var.report.drawString(400, 645, 'Fecha Factura: ')
                var.report.setFont('Helvetica', size=9)
                var.report.drawString(55, 660, 'DNI/CIF: ', str(dni))
                var.report.drawString(480, 660, str(nfac))
                var.report.drawString(480, 645, str(fechafac))
                var.report.drawString(55, 645, 'Nombre: ', str(cliente[0]))
                var.report.drawString(55, 630, 'Direccion: ', str(cliente[2]))
                var.report.drawString(55, 615, 'Municipio: ', str(cliente[4]))
                var.report.drawString(55, 600, 'Provincia: ', str(cliente[3]))

                #para abrir la factura
                var.report.save()
                rootPath = '.\\informes'
                for file in os.listdir(rootPath):
                    if file.endswith('factura.pdf'):
                        os.startfile('%s\%s' % (rootPath, file))
        except Exception as error:
            print("Error factura: ", error)
