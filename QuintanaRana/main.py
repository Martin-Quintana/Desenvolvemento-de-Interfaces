import facturas
import servicios
import styles
from ventMain import *
from dlgSalir import *
from dlgCalendar import *
from datetime import *
from dlgDatos import *
import sys, var, events, clientes, conexion, informes
from PyQt6 import QtWidgets, QtCore, QtGui, QtSql

class FileDialogAbrir(QtWidgets.QFileDialog):
    '''

    Class FileDialogAbrir inherits from QFileDialog
    Esta clase se encarga de abrir el dialogo de abrir fichero

    '''
    def __int__(self):
        super(FileDialogAbrir, self).__int__()

class DialogDatos(QtWidgets.QDialog):
    '''

    Class DialogDatos inherits from QDialog
    Esta clase se encarga de abrir el dialogo de datos a exportar

    '''

    def __init__(self):
        '''

        Funcion que inicializa el dialogo de datos a exportar

        '''
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
        var.dlgdatos.btnExportaDatos.clicked.connect(events.Eventos.exportar_datos)

    def updatecli(self, state, chk):
        '''

        Funcion que actualiza el estado del checkbox de clientes

        '''
        var.statecli = state

    def updatecar(self, state, chk):
        '''

        Funcion que actualiza el estado del checkbox de coches

        '''
        var.statecar = state




class DialogCalendar(QtWidgets.QDialog):
    '''

    Class DialogCalendar inherits from QDialog
    Esta clase se encarga de abrir el dialogo de calendario

    '''
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_dlgCalendar()
        var.dlgcalendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate(QtCore.QDate(ano, mes, dia))
        var.dlgcalendar.Calendar.clicked.connect(clientes.Clientes.cargar_fecha)

class DialogSalir(QtWidgets.QDialog):
    '''

    Class DialogSalir inherits from QDialog
    Esta clase se encarga de abrir el dialogo de salir

    '''
    def __init__(self):
        '''

        Funcion que inicializa el dialogo de salir
        '''
        super(DialogSalir, self).__init__()
        var.avisosalir = Ui_dlgSalir()
        var.avisosalir.setupUi(self)

class Main(QtWidgets.QMainWindow):
    '''

    Class Main inherits from QMainWindow
    Esta clase se encarga de abrir la ventana principal y contiene todas las acciones de los botones y eventos
    '''
    def __init__(self):
        '''

        Funcion que inicializa la ventana principal

        '''
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
        var.ui.txtDni.editingFinished.connect(clientes.Clientes.mostrar_valido_dni)
        var.ui.txtNombre.editingFinished.connect(events.Eventos.letras_capital)
        var.ui.txtDirCli.editingFinished.connect(events.Eventos.letras_capital)
        var.ui.txtMatricula.editingFinished.connect(events.Eventos.letras_capital)
        var.ui.txtMarca.editingFinished.connect(events.Eventos.letras_capital)
        var.ui.txtModelo.editingFinished.connect(events.Eventos.letras_capital)
        '''
        Listados de eventos de botones
        '''
        # Botones de la pestaña de clientes
        var.ui.btnFechaltacli.clicked.connect(events.Eventos.abrir_calendario)
        var.ui.btnLimpiacli.clicked.connect(clientes.Clientes.limpiar_cliente)
        var.ui.btnGuardacli.clicked.connect(conexion.Conexion.comprobar_campos_validos)
        var.ui.btnBorracli.clicked.connect(clientes.Clientes.borrar_cliente)
        var.ui.btnModifcli.clicked.connect(clientes.Clientes.modificar_cliente)
        var.ui.btnBuscacli.clicked.connect(conexion.Conexion.buscar_coche)

        # Botones de la pestaña de Servicios
        var.ui.btnLimpiaSer.clicked.connect(servicios.Servicios.limpia_servicio)
        var.ui.btnGuardaservicio.clicked.connect(servicios.Servicios.guarda_servicio)
        var.ui.btnModifservicio.clicked.connect(conexion.Conexion.modificar_servicio)
        var.ui.btnBorraservicio.clicked.connect(conexion.Conexion.eliminar_servicio)
        var.ui.btnGuardaservicio.clicked.connect(conexion.Conexion.mostrar_tab_ventas)

        # Botones de la pestaña de Facturas
        var.ui.btnAltaFac.clicked.connect(conexion.Conexion.alta_factura)
        var.ui.btnBorraFac.clicked.connect(conexion.Conexion.borrar_factura)
        '''
        Listado de eventos de acciones
        '''

        var.ui.actionSalir.triggered.connect(events.Eventos.salir)
        var.ui.actionSalibar.triggered.connect(events.Eventos.salir)
        var.ui.actionCrear_copia_seguridad.triggered.connect(events.Eventos.crea_backup)
        var.ui.actionRestaurar_copia_seguridad.triggered.connect(events.Eventos.restaura_backup)
        var.ui.actionpushDB.triggered.connect(events.Eventos.crea_backup)
        var.ui.actionpullDB.triggered.connect(events.Eventos.restaura_backup)
        var.ui.actionExportar_Datos.triggered.connect(events.Eventos.datos)
        var.ui.actionImportar_Datos.triggered.connect(events.Eventos.importarDatos)
        var.ui.actionInformes_Clientes.triggered.connect(informes.Informes.list_clientes)
        var.ui.actionInformes_Vehiculos.triggered.connect(informes.Informes.list_autos)

        var.ui.btnInformeCoche.clicked.connect(informes.Informes.list_autos)
        var.ui.btnInformeCliente.clicked.connect(informes.Informes.list_clientes)

        '''
        Llamadas a funciones
        '''

        conexion.Conexion.conexion()
        conexion.Conexion.cargar_provincia()
        var.ui.chkHistorico.clicked.connect(conexion.Conexion.mostrar_tabla_coches_cliente)

        '''
        Funciones relacionadas con las tablas
        '''

        # Tabla de clientes
        conexion.Conexion.mostrar_tabla_coches_cliente(self)
        var.ui.tabClientes.clicked.connect(clientes.Clientes.cargar_cliente)
        var.ui.tabClientes.clicked.connect(facturas.Facturas.cargar_cliente)
        var.ui.tabFacturas.clicked.connect(conexion.Conexion.cargar_factura)

        # Tabla de Facturas
        conexion.Conexion.mostrar_tab_ventas(self)
        facturas.Facturas.carga_linea_venta(self)
        conexion.Conexion.mostrar_tab_facturas(self)
        var.ui.tabFacturas.clicked.connect(conexion.Conexion.cargar_precio)

        # Tabla de Servicios
        conexion.Conexion.mostrar_tab_servicios(self)
        var.ui.tabServicios.clicked.connect(servicios.Servicios.carga_servicio)


        '''
        Llamadas a eventos de ComboBox
        '''

        var.ui.cmbProcli.currentIndexChanged.connect(conexion.Conexion.seleccionar_municipio)
        var.cmbServicio.currentIndexChanged.connect(conexion.Conexion.cargar_precio)
        var.txtUnidades.textChanged.connect(facturas.Facturas.calcular_subtotal_servicio)
        var.ui.btnAddFila.clicked.connect(conexion.Conexion.add_venta)


        '''
        Estilos
        '''

        events.Eventos.resize_tab_coche_cliente(self)
        events.Eventos.resizeTabVentas(self)
        events.Eventos.resizeTabServicios(self)
        events.Eventos.resize_Tab_Facturas(self)
        styles.TableClientes.set_row_color()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
