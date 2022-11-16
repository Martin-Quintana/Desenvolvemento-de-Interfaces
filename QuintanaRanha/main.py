import styles
from ventMain import *
from dlgSalir import *
from dlgCalendar import *
from datetime import *
import sys, var, events, clientes, conexion

'''
Clase FileDialogAbrir
'''
class FileDialogAbrir (QtWidgets.QFileDialog):
    def __int__(self):
        super(FileDialogAbrir, self).__int__()

'''
Clase DialogDatos

class DialogDatos(QtWidgets.QDialog):
    def __int__(self):
        super(DialogDatos, self).__int__()
        var.dlgdatos = Ui_dlgDatos()
        var.dlgdatos.setupUi(self)
        
        var.dlgdatos.btnExportarDatos.clicked.connect
'''

'''
Clase DialogCalendar
'''
class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_dlgCalendar()
        var.dlgcalendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate(QtCore.QDate(ano, mes, dia))
        var.dlgcalendar.Calendar.clicked.connect(clientes.Clientes.cargaFecha)

'''
Clase DialogSalir
'''
class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.avisosalir = Ui_dlgSalir()
        var.avisosalir.setupUi(self)

'''
Clase Main
'''
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_ventMain()
        var.ui.setupUi(self)
        var.avisosalir = DialogSalir()
        var.dlgcalendar = DialogCalendar()
        var.dlgabrir = FileDialogAbrir()
        '''
        Listados de eventos de texto
        '''
        var.ui.txtDni.editingFinished.connect(clientes.Clientes.mostrarValidoDNI)
        var.ui.txtNombre.editingFinished.connect(events.Eventos.letrasCapital)
        var.ui.txtDirCli.editingFinished.connect(events.Eventos.letrasCapital)
        var.ui.txtMatricula.editingFinished.connect(events.Eventos.letrasCapital)
        var.ui.txtMarca.editingFinished.connect(events.Eventos.letrasCapital)
        var.ui.txtModelo.editingFinished.connect(events.Eventos.letrasCapital)
        '''
        Listados de eventos de botones
        '''
        var.ui.btnGuardacli.clicked.connect(clientes.Clientes.guardaCli)
        var.ui.btnFechaltacli.clicked.connect(events.Eventos.abrirCalendar)
        var.ui.btnLimpiacli.clicked.connect(clientes.Clientes.limpiaCli)
        '''
        Listado de eventos de acciones
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.actionSalibar.triggered.connect(events.Eventos.Salir)
        var.ui.actionCrear_copia_seguridad.triggered.connect(events.Eventos.creaBackup)
        var.ui.actionRestaurar_copia_seguridad.triggered.connect(events.Eventos.restauraBackup)
        var.ui.actionpushDB.triggered.connect(events.Eventos.creaBackup)
        var.ui.actionpullDB.triggered.connect(events.Eventos.restauraBackup)
        var.ui.actionExportar_Datos.triggered.connect(events.Eventos.exportarDatos)

        '''
        Llamadas a funciones
        '''
        conexion.Conexion.conexion()
        conexion.Conexion.cargarProvincia()



        '''
        Funciones relacionadas con las tablas
        '''
        conexion.Conexion.mostrarTabcarcli(self)

        var.ui.tabClientes.clicked.connect(clientes.Clientes.cargaCliente)

        '''
        Llamadas a eventos de ComboBox
        '''
        var.ui.cmbProcli.currentIndexChanged.connect(conexion.Conexion.selMuni)

        '''
        Estilos
        '''
        events.Eventos.resizeTablacarcli(self)
        styles.TableClientes.setRowColor()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
