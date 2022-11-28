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
    Metodo que sirve para salir del programa y ademas llama a una ventana emergente que te pregunta si estas seguro
    en salir del programa
    '''
    def Salir(self):
        try:
            # Mostramos la ventana de aviso salir
            var.avisosalir.show()
            if var.avisosalir.exec():
                sys.exit()
            else:
                # Escondemos la ventana de aviso salir
                var.avisosalir.hide()
            # sys.exit()
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al Salir')
            msg.exec()
            print(error)


    '''
    Metodo que sirve para abrir la ventana del Calendario
    '''
    def abrirCalendar(self=None):
        try:
            # Mostramos la ventana del calendario
            var.dlgcalendar.show()
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al mostrar Calendario ')
            msg.exec()
            print(error)

    def datos(self):
        try:
            var.dlgdatos.show()
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al abrir Exportar Datos ')
            msg.exec()
            print(error)

    '''
    Metodo que sirve para poner las primeras letras de cada palabra en mayuscula
    '''
    def letrasCapital(self=None):
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
            msg.setText('Error al poner en mayusculas ')
            msg.exec()
            print(error)

    '''
    Metodo que sirve para que el tamanho de las celdas de la tabla sea el adecuado
    '''
    def resizeTablacarcli(self):
        try:
            # Seleccionamos el cabecero de la tabla
            header = var.ui.tabClientes.horizontalHeader()
            # Redimensionamos la Tabla
            for i in range(5):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                if i == 1 or i == 1:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al deimensionar la table de coches')
            msg.exec()
            print(error)


    '''
    Metodo que sirve para crear un backup de la base de datos 
    '''
    def creaBackup(self):
        try:
            # Declaramos las variables fecha, copia, directorio y filename
            fecha = datetime.today()
            fecha = fecha.strftime('%Y-%m-%d-%H.%M.%S')
            copia = (str(fecha) + '_backup.zip')
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Copia',
                                                                copia, '.zip')
            # Creamos la Backup
            if var.dlgabrir.accept and filename != '':
                fichzip = zipfile.ZipFile(copia, 'w')
                fichzip.write(var.bbdd, os.path.basename(var.bbdd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(copia), str(directorio))

                # Mensaje de informacion
                msg = QtWidgets.QMessageBox()
                msg.setModal(True)
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Copia de Seguridad Creada')
                msg.exec()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al crear una copia de seguridad ')
            msg.exec()
            print(error)


    '''
    Metodo que sirve para restaurar las copias de seguridad
    '''
    def restauraBackup(self = None):
        try:
            # Declaramos la variable
            filename = var.dlgabrir.getOpenFileName(None,
                                                    'Restaurar copia de seguridad',
                                                    '',
                                                    'All Files (*);;zip (*.zip)')
            if var.dlgabrir.accept and filename != '':
                file = filename[0]
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None, path='./db')
                bbdd.close()
            conexion.Conexion.conexion()
            conexion.Conexion.mostrarTabcarcli()

            # Mensaje de informacion
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
            msg.setText('Error al restaurar el Backup ')
            msg.exec()
            print(error)


    '''
    Metodo que sirve para exportar los datos de la base de datos
    '''
    def exportarDatos(self = None):
        try:
            var.dlgdatos.hide()

            if var.chkCoches.isChecked():
                print('Coche')
            if var.chkClientes.isChecked():
                print('Cliente')


            fecha = datetime.today()
            fecha = fecha.strftime('%Y-%m-%d-%H.%M.%S')
            file = (str(fecha) + '_Clientes.xls')

            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Datos',
                                                                file, '.xls')
            wb = xlwt.Workbook()
            sheet1 = wb.add_sheet('Clientes')
            sheet1.write(0,0,'DNI')
            sheet1.write(0,1,'Nombre')
            sheet1.write(0,2,'Fecha Alta')
            sheet1.write(0,3,'Direccion')
            sheet1.write(0,4,'Provincia')
            sheet1.write(0,5,'Municipio')
            sheet1.write(0,6,'Forma de Pago')
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
            msg.setText('Exportacion de Datos Realizada')
            msg.exec()


        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al Exportar Datos ')
            msg.exec()
            print(error)



    '''
    Metodo que sirve para Importar Datos de Excel
    '''
    def importarDatos(self):
        try:
            #Llamamos al explorador de Windows para poder buscar el archivo
            filename = var.dlgabrir.getOpenFileName(None, 'Guardar Datos ',
                                                    '','*xls;;All Files (*)')
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
                        new =  []
                        for j in range(columnas):
                            new.append(str(datos.cell_value(i,j)))
                        if clientes.Clientes.validarDNI(str(new[1])):
                            conexion.Conexion.altaExcelCoche(new)

                #Mensaje de aviso que la importacion de Datos ha sido Realizada
                msg = QtWidgets.QMessageBox()
                msg.setModal(True)
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Importacion de Datos Realizada')
                msg.exec()
                conexion.Conexion.mostrarTabcarcli(self)




        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al guardar la importacion de datos')
            msg.exec()
            print(error)














