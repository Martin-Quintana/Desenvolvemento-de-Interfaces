import sys
from PyQt6 import QtWidgets, QtSql

import sys,var

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
            #sys.exit()
        except Exception as error:
            print("Error en función salir %s", str(error))

    def abrirCalendar (self = None):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error abrir calendario', error)

    def letrasCapital (self = None):
        try:
            var.ui.txtNombre.setText(var.ui.txtNombre.text().title())
            var.ui.txtDirCli.setText(var.ui.txtDirCli.text().title())
            var.ui.txtMatricula.setText(var.ui.txtMatricula.text().upper())
            var.ui.txtMarca.setText(var.ui.txtMarca.text().upper())
            var.ui.txtModelo.setText(var.ui.txtModelo.text().upper())
        except Exception as error:
            print('Error al poner mayusculas', error)

    '''
    Poner la Tabla bonita y Fresca
    '''

    def resizeTablacarcli(self = None):
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(5):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                if i == 0 or i == 1:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        except Exception as error:
            print('', error)
