import os, var
from PyQt6 import QtSql, QtWidgets
from reportlab.pdfgen import canvas
from datetime import datetime

import conexion


class Informes:
    def list_clientes(self):
        """

        Funcion que genera el listado de clientes en un pdf con reportlab
        :return:  pdf con listado de clientes

        """
        try:
            var.report = canvas.Canvas('informes/listadoClientes.pdf')
            titulo = 'LISTADO CLIENTES'
            Informes.pie_informe(titulo)
            Informes.top_informe(titulo)

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
                        Informes.top_informe(titulo)
                        Informes.pie_informe(titulo)
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

            rootpath = '.\\informes\\'
            ruta_informe = os.path.join(rootpath, 'listadoClientes.pdf')
            os.startfile(ruta_informe)



        except Exception as error:
            print('Error informes estado cliente', error)

    def list_autos(self):
        """

        Funcion que genera el listado de vehiculos en un pdf con reportlab
        :return:  pdf con listado de vehiculos

        """
        try:
            var.report = canvas.Canvas('informes/listadoAutos.pdf')
            titulo = 'LISTADO VEHICULOS'
            Informes.pie_informe(titulo)
            Informes.top_informe(titulo)

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
                        Informes.top_informe(titulo)
                        Informes.pie_informe(titulo)
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


            rootpath = '.\\informes\\'
            ruta_informe = os.path.join(rootpath, 'listadoAutos.pdf')
            os.startfile(ruta_informe)
        except Exception as error:
            print('Error informes estado vehiculos', error)

    def top_informe(titulo):
        """

        Funcion que genera el top del informe
        :param titulo: titulo del informe
        :return:  top del informe

        """
        try:
            logo = '.\img\logo-aston-martin.png'
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

    def pie_informe(titulo):
        """

        Funcion que genera el pie del informe
        :return:  pie del informe

        """
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
        """

        Funcion que genera el informe de la factura
        :return:  informe de la factura

        """
        try:
            i = 60
            j = 530
            var.report = canvas.Canvas('informes/factura.pdf')
            titulo = 'FACTURA'
            Informes.pie_informe(titulo)
            Informes.top_informe(titulo)

            items = ['ID', 'SERVICIO', 'PRECIO', 'CANTIDAD', 'TOTAL']

            cliente = []

            dni = str(var.ui.txtDniFac.text())

            query3 = QtSql.QSqlQuery()
            query3.prepare('select dni, nombre, alta, direccion, provincia, municipio, pago from clientes where dni = :dni')
            query3.bindValue(':dni', dni)

            if query3.exec():
                while query3.next():
                    dni = str(query3.value(0))
                    nombre = str(query3.value(1))
                    alta = str(query3.value(2))
                    direccion = str(query3.value(3))
                    provincia = str(query3.value(4))
                    municipio = str(query3.value(5))
                    pago = str(query3.value(6))



            dni = str(var.ui.txtDniFac.text())
            nfac = str(var.ui.txtFactura.text())
            fechafac = str(var.ui.txtFechaFac.text())

            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(55, 660, 'DATOS DEL CLIENTE')
            var.report.line(50, 650, 525, 650)
            var.report.drawString(55, 640, 'DNI: ' + dni)
            var.report.drawString(55, 630, 'Nombre: ' + nombre)
            var.report.drawString(55, 620, 'Fecha de alta: ' + alta)
            var.report.drawString(55, 610, 'Direccion: ' + direccion)
            var.report.drawString(55, 600, 'Provincia: ' + provincia)
            var.report.drawString(55, 590, 'Municipio: ' + municipio)
            var.report.drawString(55, 580, 'Forma de pago: ' + pago)
            var.report.line(50, 560, 525, 560)

            query3 = QtSql.QSqlQuery()
            query3.prepare('select idVentas, codServ, unidades, precio, subtotal from ventas where codFac = :codFac')
            query3.bindValue(':codFac', int(nfac))

            if query3.exec():
                while query3.next():
                    query2 = QtSql.QSqlQuery()
                    query2.prepare('select concepto from servicios where codigo = :codServ')
                    query2.bindValue(':codServ', query3.value(1))
                    if query2.exec():
                        while query2.next():
                            var.report.drawString(i, j, 'ID: ' + str(query3.value(0)))
                            var.report.drawString(i + 50, j, 'Servicio: ' + str(query2.value(0)))
                            var.report.drawString(i + 200, j, 'Precio: ' + str(query3.value(3)))
                            var.report.drawString(i + 300, j, 'Cantidad: ' + str(query3.value(2)))
                            var.report.drawString(i + 400, j, 'Total: ' + str(query3.value(4)))

                            j -= 20



            var.report.save()
            rootpath = '.\\informes'
            ruta_informe = os.path.join(rootpath, 'factura.pdf')
            os.startfile(ruta_informe)

        except Exception as error:
            print("Error factura: ", error)
