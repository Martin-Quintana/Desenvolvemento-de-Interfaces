import datetime

from PyQt6 import QtSql
from datetime import datetime
import clientes
import var, os
from ventMain import *

# Clase que se utilizara para controlar las utilidades de la ventana servicios

class Servicios():

    def guardarServicios(self=None):
        try:
            concepto = var.ui.txtConcepto
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al cargar las provincias')
            print(error)
            msg.exec()

