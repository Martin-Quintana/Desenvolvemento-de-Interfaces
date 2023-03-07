import zipfile
from dlgDatos import *
from PyQt6 import QtWidgets, QtSql
from datetime import datetime, date

import sys, var, shutil, os, xlwt, conexion, xlrd

import clientes

'''
Eventos generales
'''


class Eventos:
    '''

    Class Eventos
    Esta clase se encarga de los eventos de la aplicacion

    '''

    def salir(self):
        """

        Funcion que cierra la aplicacion
        :return:  None

        """
        try:
            var.avisosalir.show()
            if var.avisosalir.exec():
                sys.exit()
            else:
                var.avisosalir.hide()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al Salir')
            msg.exec()
            print(error)

    '''
    Abrir calendario
    '''

    def abrir_calendario(self=None):
        """

        Funcion que abre el calendario
        :return:  None
        """
        try:
            var.dlgcalendar.show()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error mostrar Calendario ')
            msg.exec()
            print(error)


    def datos(self):
        """

        Funcion que abre la ventana de datos de la aplicacion
        :return:  None
        """
        try:
            var.dlgdatos.show()
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al abrir Exportar Datos ')
            msg.exec()
            print(error)


    def letras_capital(self=None):
        """

        Funcion que pone en mayusculas el texto de los campos de texto
        :return:  None

        """
        try:
            var.ui.txtNombre.setText(var.ui.txtNombre.text().title())
            var.ui.txtDirCli.setText(var.ui.txtDirCli.text().title())
            var.ui.txtMatricula.setText(var.ui.txtMatricula.text().upper())
            var.ui.txtMarca.setText(var.ui.txtMarca.text().upper())
            var.ui.txtModelo.setText(var.ui.txtModelo.text().upper())

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al poner mayusculas')
            msg.exec()
            print(error)



    def resize_tab_coche_cliente(self):
        """

        Funcion que redimensiona la tabla de coches de los clientes
        :return:  None

        """
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(5):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                if i == 1 or i == 1:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error dimensionar tabla coches')
            msg.exec()
            print(error)



    def crea_backup(self):
        """

        Funcion que crea un backup de la base de datos
        :return:  None

        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y-%m-%d-%H.%M.%S')
            copia = (str(fecha) + '_backup.zip')
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Copia', copia, '.zip')

            if var.dlgabrir.accept and filename != '':
                fichzip = zipfile.ZipFile(copia, 'w')
                fichzip.write(var.bbdd, os.path.basename(var.bbdd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(copia), str(directorio))

                msg = QtWidgets.QMessageBox()
                msg.setModal(True)
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Copia de seguridad creada')
                msg.exec()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error BackUp')
            msg.exec()
            print(error)


    def restaura_backup(self=None):
        """

        Funcion que restaura un backup de la base de datos
        :return: None

        """
        try:
            filename = var.dlgabrir.getOpenFileName(None, 'Restaurar copia de seguridad', '', 'All Files (*);;zip (*.zip)')

            if var.dlgabrir.accept and filename != '':
                file = filename[0]
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None, path='./db')
                bbdd.close()

            conexion.Conexion.conexion()
            conexion.Conexion.mostrar_tabla_coches_cliente(self)

            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Copia de seguridad restaurada')
            msg.exec()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error restaurar BackUp ')
            msg.exec()
            print(error)


    def exportar_datos(self=None):
        """

        Funcion que exporta los datos de la base de datos a un fichero excel
        :return:  None

        """
        try:
            var.dlgdatos.hide()
            fecha = datetime.today()
            fecha = fecha.strftime('%Y-%m-%d-%H.%M.%S')
            file = (str(fecha) + 'Datos exportados.xls')

            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Datos', file, '.xls')
            wb = xlwt.Workbook()

            if var.chkCoches.isChecked():
                sheet1 = wb.add_sheet('Coches')
                sheet1.write(0, 0, 'DNI')
                sheet1.write(0, 1, 'Matricula')
                sheet1.write(0, 2, 'Marca')
                sheet1.write(0, 3, 'Modelo')
                fila = 1

                query = QtSql.QSqlQuery()
                query.prepare('select *  from coches order by matricula')

                if query.exec():
                    while query.next():
                        sheet1.write(fila, 0, str(query.value(0)))
                        sheet1.write(fila, 1, str(query.value(1)))
                        sheet1.write(fila, 2, str(query.value(2)))
                        sheet1.write(fila, 3, str(query.value(3)))
                        fila += 1

            if var.chkClientes.isChecked():
                sheet1 = wb.add_sheet('Clientes')
                sheet1.write(0, 0, 'DNI')
                sheet1.write(0, 1, 'Nombre')
                sheet1.write(0, 2, 'Fecha Alta')
                sheet1.write(0, 3, 'Direccion')
                sheet1.write(0, 4, 'Provincia')
                sheet1.write(0, 5, 'Municipio')
                sheet1.write(0, 6, 'Forma de Pago')
                fila = 1

                query = QtSql.QSqlQuery()
                query.prepare('select *  from clientes order by dni')

                if query.exec():
                    while query.next():
                        sheet1.write(fila, 0, str(query.value(0)))
                        sheet1.write(fila, 1, str(query.value(1)))
                        sheet1.write(fila, 2, str(query.value(2)))
                        sheet1.write(fila, 3, str(query.value(3)))
                        sheet1.write(fila, 4, str(query.value(4)))
                        sheet1.write(fila, 5, str(query.value(5)))
                        sheet1.write(fila, 6, str(query.value(6)))
                        fila += 1

            wb.save(directorio)

            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Exportacion realizaca')
            msg.exec()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error exportar')
            msg.exec()
            print(error)


    def importarDatos(self):
        """

        Funcion que importa los datos de un fichero excel a la base de datos
        :return None

        """
        try:
            filename = var.dlgabrir.getOpenFileName(None, 'Guardar Datos ', '', '*xls;;All Files (*)')
            if var.dlgabrir.accept and filename != '':
                file = filename[0]
                documento = xlrd.open_workbook(file)
                datos = documento.sheet_by_index(0)
                filas = datos.nrows
                columnas = datos.ncols

                new = []
                for i in range(filas):
                    if i == 0:
                        pass
                    else:
                        new = []
                        for j in range(columnas):
                            new.append(str(datos.cell_value(i, j)))
                        if clientes.Clientes.validar_dni(str(new[1])):
                            conexion.Conexion.alta_excel_coche(new)


                msg = QtWidgets.QMessageBox()
                msg.setModal(True)
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Importacion realizada')
                msg.exec()
                conexion.Conexion.mostrar_tabla_coches_cliente(self)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error imporatcion')
            msg.exec()
            print(error)


    def resizeTabVentas(self):
        """

        Funcion que redimensiona la tabla de ventas
        :return:  None
        """
        try:
            header = var.ui.tabVentas.horizontalHeader()
            for i in range(3):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                if i == 1 or i == 1:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error dimensionar tabla Ventas')
            msg.exec()
            print(error)

    def resizeTabServicios(self):
        """

        Funcion que redimensiona la tabla de servicios
        :return:  None

        """
        try:
            header = var.ui.tabServicios.horizontalHeader()
            for i in range(2):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                if i == 1 or i == 1:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error dimensionar tabla Servicios')
            msg.exec()
            print(error)

    def resize_Tab_Facturas(self):
        """

        Funcion que redimensiona la tabla de facturas
        :return:  None
        """
        try:
            header = var.ui.tabFacturas.horizontalHeader()
            for i in range(2):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                if i == 1 or i == 1:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error dimensionar tabla Facturas')
            msg.exec()
            print(error)
