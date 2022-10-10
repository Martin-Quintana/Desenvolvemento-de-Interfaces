from ventMain import *
from dlgSalir import *
from dlgCalendar import *
import sys, var, events, clientes, datetime

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_dlgCalendar()
        var.dlgcalendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        var.dlgcalendar.Calendaralendar.setSelectedDate(QtCore.QDate(ano, mes, dia))
        var.dlgcalendar.Calendar.clicked.connect(clientes.Clientes.cargaFecha)

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
        var.dlgcalendar = DialogCalendar()
        '''
        Listados de eventos
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.txtDni.editingFinished.connect(clientes.Clientes.mostrarValidoDNI)
        var.ui.actionSalibar.triggered.connect(events.Eventos.Salir)
        var.ui.btnGuardacli.clicked.connect(clientes.Clientes.guardaCli)
        var.ui.btnFechaltacli.clicked.connect(events.Eventos.abrirCalendar)
        '''
        Listados de eventos
        '''



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
