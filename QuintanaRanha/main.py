from ventMain import *
from dlgSalir import *
import sys, var, events, clientes

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.avisosalir = Ui_dlgSalir()
        var.avisosalir.setupUi(self)


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
        var.ui.actionSalirbar.triggered.connect(events.Eventos.Salir)
        var.ui.txtDni.editingFinished.connect(clientes.Clientes.mostrarValidoDNI)
        '''
        Listados de eventos
        '''
        clientes.Clientes.selMotor(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
