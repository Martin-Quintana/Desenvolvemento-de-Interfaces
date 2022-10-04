from PyQt6.QtWidgets import QDialog

from ventMain import *
from dlgSalir import *
import sys,var,events,clientes

class DialogSalir(QtWidgets.QDialog):
    def __int__(self):
        super(DialogSalir, self).__int__()
        var.avisosalir = Ui_dlgSalir()
        var.avisosalir.setupUi(self)
        #var.avisosalir.btnSalir.clicked.connect(events.Eventos.Salir)


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_ventMain()
        var.ui.setupUi(self)
        var.avisosalir = DialogSalir()
        '''
        Listados de eventos
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.txtDni.editingFinished.connect(clientes.Clientes.mostrarValidoDNI)

        '''
        LLamadas a funciones
        '''
        clientes.Clientes.selMotor(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
