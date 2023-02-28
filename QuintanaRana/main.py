import facturas
import servicios
import styles
from ventMain import *
from dlgSalir import *
from dlgCalendar import *
from datetime import *
from dlgDatos import *
from PyQt6 import *
import sys, var, events, clientes, conexion, informes

'''
FileDialogAbrir
'''


class FileDialogAbrir(QtWidgets.QFileDialog):
    def __int__(self):
        super(FileDialogAbrir, self).__int__()


'''
DialogDatos
'''


class DialogDatos(QtWidgets.QDialog):
    def __init__(self):
        super(DialogDatos, self).__init__()
        var.dlgdatos = Ui_dlgDatos()
        var.dlgdatos.setupUi(self)
        var.chkClientes = var.dlgdatos.chkClientes
        var.chkCoches = var.dlgdatos.chkCoches

        var.statecar = 0
        var.statecli = 0

        var.dlgdatos.chkClientes.stateChanged.connect(
            lambda state, chkcli=var.dlgdatos.chkClientes: self.updatecli(state, chkcli))
        var.dlgdatos.chkCoches.stateChanged.connect(
            lambda state, chkcar=var.dlgdatos.chkCoches: self.updatecar(state, chkcar))
        var.dlgdatos.btnExportaDatos.clicked.connect(events.Eventos.exportarDatos)

    def updatecli(self, state, chk):
        var.statecli = state

    def updatecar(self, state, chk):
        var.statecar = state


'''
DialogCalendar
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
DialogSalir
'''


class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.avisosalir = Ui_dlgSalir()
        var.avisosalir.setupUi(self)


'''
Main
'''


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_ventMain()
        var.ui.setupUi(self)
        var.avisosalir = DialogSalir()
        var.dlgcalendar = DialogCalendar()
        var.dlgabrir = FileDialogAbrir()
        var.dlgdatos = DialogDatos()

        '''
        Listados de eventos de texto
        '''

        # Eventos tipo texto de la pestaña de clientes
        var.ui.txtDni.editingFinished.connect(clientes.Clientes.mostrarValidoDNI)
        var.ui.txtNombre.editingFinished.connect(events.Eventos.letrasCapital)
        var.ui.txtDirCli.editingFinished.connect(events.Eventos.letrasCapital)
        var.ui.txtMatricula.editingFinished.connect(events.Eventos.letrasCapital)
        var.ui.txtMarca.editingFinished.connect(events.Eventos.letrasCapital)
        var.ui.txtModelo.editingFinished.connect(events.Eventos.letrasCapital)
        '''
        Listados de eventos de botones
        '''
        # Botones de la pestaña de clientes
        var.ui.btnFechaltacli.clicked.connect(events.Eventos.abrirCalendar)
        var.ui.btnLimpiacli.clicked.connect(clientes.Clientes.limpiaCli)
        var.ui.btnGuardacli.clicked.connect(conexion.Conexion.comprobarCamposValidos)
        var.ui.btnBorracli.clicked.connect(clientes.Clientes.borraCli)
        var.ui.btnModifcli.clicked.connect(clientes.Clientes.modifCli)
        var.ui.btnBuscacli.clicked.connect(conexion.Conexion.buscaCoche)

        # Botones de la pestaña de Servicios
        var.ui.btnLimpiaSer.clicked.connect(servicios.Servicios.limpiaServicio)
        var.ui.btnGuardaservicio.clicked.connect(servicios.Servicios.guardaServicio)
        var.ui.btnModifservicio.clicked.connect(conexion.Conexion.modServicio)
        var.ui.btnBorraservicio.clicked.connect(conexion.Conexion.delServicio)
        var.ui.btnGuardaservicio.clicked.connect(conexion.Conexion.mostrarTabVentas)

        '''
        Listado de eventos de acciones
        '''

        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.actionSalibar.triggered.connect(events.Eventos.Salir)
        var.ui.actionCrear_copia_seguridad.triggered.connect(events.Eventos.creaBackup)
        var.ui.actionRestaurar_copia_seguridad.triggered.connect(events.Eventos.restauraBackup)
        var.ui.actionpushDB.triggered.connect(events.Eventos.creaBackup)
        var.ui.actionpullDB.triggered.connect(events.Eventos.restauraBackup)
        var.ui.actionExportar_Datos.triggered.connect(events.Eventos.datos)
        var.ui.actionImportar_Datos.triggered.connect(events.Eventos.importarDatos)
        var.ui.actionInformes_Clientes.triggered.connect(informes.Informes.listClientes)
        var.ui.actionInformes_Vehiculos.triggered.connect(informes.Informes.listAutos)

        '''
        Llamadas a funciones
        '''

        conexion.Conexion.conexion()
        conexion.Conexion.cargarProvincia()
        var.ui.chkHistorico.clicked.connect(conexion.Conexion.mostrarTabcarcli)

        '''
        Funciones relacionadas con las tablas
        '''

        # Tabla de clientes
        conexion.Conexion.mostrarTabcarcli(self)
        var.ui.tabClientes.clicked.connect(clientes.Clientes.cargaCliente)
        var.ui.tabClientes.clicked.connect(facturas.Facturas.cargaCliente)

        # Tabla de Facturas
        conexion.Conexion.mostrarTabVentas(self)
        facturas.Facturas.cargaLineaVenta(self)


        # Tabla de Servicios
        conexion.Conexion.mostrarTabservicios(self)
        var.ui.tabServicios.clicked.connect(servicios.Servicios.cargaServicio)


        '''
        Llamadas a eventos de ComboBox
        '''

        var.ui.cmbProcli.currentIndexChanged.connect(conexion.Conexion.selMuni)
        var.cmbServicio.currentIndexChanged.connect(conexion.Conexion.cargaPrecio)
        var.txtUnidades.textChanged.connect(facturas.Facturas.calcularSubtotalServicio)
        # var.ui.btnAddFila.clicked.connect(conexion.Conexion.add_Venta)


        '''
        Estilos
        '''

        events.Eventos.resizeTablacarcli(self)
        events.Eventos.resizeTabVentas(self)
        events.Eventos.resizeTabServicios(self)
        styles.TableClientes.setRowColor()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
