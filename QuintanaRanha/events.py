import zipfile

from PyQt6 import QtWidgets, QtSql
from datetime import datetime, date

import sys, var, shutil, os

'''
Eventos generales
'''


class Eventos:
    def Salir(self):
        try:
            var.avisosalir.show()
            if var.avisosalir.exec():
                sys.exit()
            else:
                var.avisosalir.hide()
            # sys.exit()
        except Exception as error:
            print("Error en función salir %s", str(error))

    def abrirCalendar(self=None):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error abrir calendario', error)

    def letrasCapital(self=None):
        try:
            var.ui.txtNombre.setText(var.ui.txtNombre.text().title())
            var.ui.txtDirCli.setText(var.ui.txtDirCli.text().title())
            var.ui.txtMatricula.setText(var.ui.txtMatricula.text().upper())
            var.ui.txtMarca.setText(var.ui.txtMarca.text().upper())
            var.ui.txtModelo.setText(var.ui.txtModelo.text().upper())
        except Exception as error:
            print('Error al poner mayusculas', error)
    def resizeTablacarcli(self):
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(5):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                if i == 1 or i == 1:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print('Error dimensionar talblero coches', error)

    def creaBackup(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H.%M.%S')
            copia = (str(fecha) + '_backup.zip')
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Copia',
                                                                copia, '.zip')
            if var.dlgabrir.accept and filename != '':
                fichzip = zipfile.ZipFile(copia, 'w')
                fichzip.write(var.bbdd, os.path.basename(var.bbdd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(copia), str(directorio))
                print('Copia de seguridad creada')





        except Exception as error:
            print('Error al crear copia de seguridad ', error)
