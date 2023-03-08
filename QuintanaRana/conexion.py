import datetime

from PyQt6 import QtSql
from datetime import datetime
import clientes
import facturas
import var
from ventMain import *


class Conexion():
    '''
    Clase conexion

    Esta clase se encarga de realizar la conexion con la base de datos

    '''

    def conexion(self=None):
        """

        Funcion que realiza la conexion con la base de datos y devuelve un booleano
        :return: True si la conexion es correcta, False si no lo es

        """
        filedb = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filedb)
        var.bbdd = 'bbdd.sqlite'
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos',
                                           'Conexion no establecida.\n', 'Haga click para cerrar',
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False
        else:
            print('Conexion establecida')
            return True


    def cargar_provincia(self=None):
        """

        Funcion que carga las provincias en el combobox de provincias de la ventana de clientes
        :return:


        """
        try:
            var.ui.cmbProcli.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec():
                var.ui.cmbProcli.addItem('')
                while query.next():
                    var.ui.cmbProcli.addItem(query.value(0))

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error cargar provincias')
            msg.exec()
            print(error)

    def seleccionar_municipio(self=None):
        """

        Funcion que carga los municipios en el combobox de municipios de la ventana de clientes en funcion de la provincia
        seleccionada
        :return:

        """
        try:
            id = 0
            var.ui.cmbMunicli.clear()
            prov = var.ui.cmbProcli.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select id from provincias where provincia = :prov')
            query.bindValue(':prov', prov)

            if query.exec():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare('select municipio from municipios where provincia_id = :id')
            query1.bindValue(':id', int(id))

            if query1.exec():
                var.ui.cmbMunicli.addItem('')
                while query1.next():
                    var.ui.cmbMunicli.addItem(query1.value(0))

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error carga municipios')
            msg.exec()
            print(error)


    def alta_cliente(newcli, newcar):
        """

        Funcion que da de alta un cliente y su vehiculo en la base de datos
        :param newcar:
        :param newcli:
        :return:
        """
        try:
            query = QtSql.QSqlQuery()
            queryCli = QtSql.QSqlQuery()
            query.prepare('insert into clientes (dni, nombre, alta, direccion, provincia, municipio, pago) '
                          'values (:dni, :nombre, :alta, :direccion, :provincia, :municipio, :pago)')
            queryCli.prepare('select dni from clientes where dni = :dni')
            queryCli.bindValue(':dni', str(newcli[0]))
            query.bindValue(':dni', str(newcli[0]))
            query.bindValue(':nombre', str(newcli[1]))
            query.bindValue(':alta', str(newcli[2]))
            query.bindValue(':direccion', str(newcli[3]))
            query.bindValue(':provincia', str(newcli[4]))
            query.bindValue(':municipio', str(newcli[5]))
            query.bindValue(':pago', str(newcli[6]))

            if query.exec():
                pass
            query1 = QtSql.QSqlQuery()
            query1.prepare('insert into coches(matricula, dnicli, marca, modelo, motor) '
                           'values (:matricula, :dnicli, :marca, :modelo, :motor)')
            query1.bindValue(':matricula', str(newcar[0]))
            query1.bindValue(':dnicli', str(newcli[0]))
            query1.bindValue(':marca', str(newcar[1]))
            query1.bindValue(':modelo', str(newcar[2]))
            query1.bindValue(':motor', str(newcar[3]))

            if query1.exec():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Coche dado de alta')
                msg.exec()

            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText(query1.lastError().text())
                msg.exec()
            Conexion.mostrar_tabla_coches_cliente(self=None)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error alta cliente')
            msg.exec()
            print(error)


    def mostrar_tabla_coches_cliente(self):
        """

        Funcion que muestra los coches de un cliente en la tabla de la ventana de clientes
        :return:

        """
        try:
            var.ui.tabClientes.clearContents()
            if var.ui.chkHistorico.isChecked() == False:
                index = 0
                query = QtSql.QSqlQuery()
                query.prepare(
                    'select matricula, dnicli, marca, modelo, motor from coches where fechabajacar is null order by marca, modelo')

                if query.exec():
                    while query.next():
                        var.ui.tabClientes.setRowCount(index + 1)
                        var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(1))))
                        var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(query.value(0))))
                        var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(query.value(2))))
                        var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(query.value(3))))
                        var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(query.value(4))))

                        var.ui.tabClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        var.ui.tabClientes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        var.ui.tabClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        var.ui.tabClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        var.ui.tabClientes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                        index += 1

            else:
                index = 0
                query = QtSql.QSqlQuery()
                query.prepare(
                    'select matricula, dnicli, marca, modelo, motor, fechabajacar from coches order by marca, modelo')

                if query.exec():
                    while query.next():
                        var.ui.tabClientes.setRowCount(index + 1)
                        var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(1))))
                        var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(query.value(0))))
                        var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(query.value(2))))
                        var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(query.value(3))))
                        var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(query.value(4))))
                        var.ui.tabClientes.setItem(index, 5, QtWidgets.QTableWidgetItem(str(query.value(5))))

                        var.ui.tabClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        var.ui.tabClientes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        var.ui.tabClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        var.ui.tabClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        var.ui.tabClientes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        var.ui.tabClientes.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                        index += 1

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error mostrar tabla ')
            msg.exec()
            print(error)


    def one_cliente(dni):
        """

        Funcion que devuelve un registro de un cliente en una lista
        :return:
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select nombre, alta, direccion, provincia, municipio, pago from clientes where dni = :dni')
            query.bindValue(':dni', str(dni))

            if query.exec():
                while query.next():
                    for i in range(6):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error carga cliente de tabla')
            msg.exec()
            print(error)


    def alta_excel_coche(new):
        """

        Funcion que da de alta un coche en la base de datos a partir de un excel
        :return:

        """
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('insert into coches(matricula, dnicli, marca, modelo, motor, fechabajacar) '
                           'values (:matricula, :dnicli, :marca, :modelo, :motor, :fechabajacar)')
            query1.bindValue(':matricula', str(new[0]))
            query1.bindValue(':dnicli', str(new[1]))
            query1.bindValue(':marca', str(new[2]))
            query1.bindValue(':modelo', str(new[3]))
            query1.bindValue(':motor', str(new[4]))
            query1.bindValue(':fechabajacar', str(new[5]))

            if query1.exec():
                pass

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error alta Excel')
            msg.exec()
            print(error)


    def comprobar_campos_validos(self=None):
        """

        Funcion que comprueba que los campos de la ventana de clientes estan rellenos
        :return:

        """
        try:
            dni = var.ui.txtDni.text()

            if clientes.Clientes.validar_dni(dni) \
                    and len(var.ui.txtNombre.text()) > 0 and len(var.ui.txtDirCli.text()) > 0 \
                    and len(var.ui.txtMatricula.text()) > 0 and len(var.ui.txtMarca.text()) > 0 \
                    and len(var.ui.txtModelo.text()) > 0 and len(var.ui.cmbProcli.currentText()) > 0 \
                    and len(var.ui.cmbMunicli.currentText()) > 0 and len(var.ui.txtFechaltacli.text()) > 0:
                clientes.Clientes.guardar_cliente()

            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('Error cargar cliente')
                msg.exec()
                return False

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error comprobar datos')
            msg.exec()
            print(error)

    def borrar_cliente(dni):
        """

        Funcion que da de baja un cliente y sus coches
        :return:

        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y-%m-%d-%H.%M.%S')

            query1 = QtSql.QSqlQuery()
            query1.prepare('update clientes set fechabajacli = :fecha where dni = :dni')
            query1.bindValue(':fecha', str(fecha))
            query1.bindValue(':dni', str(dni))

            if query1.exec():
                pass

            query = QtSql.QSqlQuery()
            query.prepare('update coches set fechabajacar = :fecha where dnicli = :dni')
            query.bindValue(':fecha', str(fecha))
            query.bindValue(':dni', str(dni))

            if query.exec():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('Cliente dado de baja')
                msg.exec()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error borrar cliente bbdd')
            msg.exec()
            print(error)


    def modificar_cliente(modcli, modcar):
        """

        Funcion que modifica un cliente y sus coches
        :param modcar:
        :return:

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update clientes set nombre = :nombre, alta = :alta,'
                          'direccion = :direccion, provincia = :provincia, municipio = :municipio,'
                          'pago = :pago where dni = :dni')
            query.bindValue(':dni', str(modcli[0]))
            query.bindValue(':nombre', str(modcli[1]))
            query.bindValue(':alta', str(modcli[2]))
            query.bindValue(':direccion', str(modcli[3]))
            query.bindValue(':provincia', str(modcli[4]))
            query.bindValue(':municipio', str(modcli[5]))
            query.bindValue(':pago', str(modcli[6]))
            if query.exec():
                pass

            query1 = QtSql.QSqlQuery()
            query1.prepare('update coches set dnicli = :dnicli, marca = :marca, modelo = :modelo,'
                           'motor = :motor where matricula = :matricula')

            query1.bindValue(':matricula', str(modcar[0]))
            query1.bindValue(':dnicli', str(modcli[0]))
            query1.bindValue(':marca', str(modcar[1]))
            query1.bindValue(':modelo', str(modcar[2]))
            query1.bindValue(':motor', str(modcar[3]))

            if query1.exec():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Coche modificado')
                msg.exec()

            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('Error al modificar Cliente')
                msg.exec()

            Conexion.mostrar_tabla_coches_cliente(self=None)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error modificar cliente bbdd')
            msg.exec()
            print(error)

    def buscar_coche(self):
        """

        Funcion que busca un coche por su matricula
        :return:  tabla con los datos del coche

        """
        try:

            var.ui.tabClientes.clearContents()

            matri = var.ui.txtMatricula.text()

            index = 0

            query = QtSql.QSqlQuery()
            query.prepare(
                'select matricula, dnicli, marca, modelo, motor, fechabajacar from coches where matricula = :matri')
            query.bindValue(':matri', matri)

            if query.exec():
                while query.next():
                    var.ui.tabClientes.setRowCount(index + 1)
                    var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(1))))
                    var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(query.value(0))))
                    var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(query.value(2))))
                    var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(query.value(3))))
                    var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(query.value(4))))
                    var.ui.tabClientes.setItem(index, 5, QtWidgets.QTableWidgetItem(str(query.value(5))))

                    var.ui.tabClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                    index += 1

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error buscar coche')
            msg.exec()
            print(error)

    # =================================================== SERVICIOS ===================================================

    def mostrar_tab_servicios(self):
        """

        Funcion que muestra los servicios en la tabla de servicios
        :rtype: object
        :return:

        """
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare(
                'select codigo, concepto, preciounidad from servicios order by codigo, concepto ')

            if query.exec():
                while query.next():
                    var.ui.tabServicios.setRowCount(index + 1)
                    var.ui.tabServicios.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(0))))
                    var.ui.tabServicios.setItem(index, 1, QtWidgets.QTableWidgetItem(str(query.value(1))))
                    var.ui.tabServicios.setItem(index, 2, QtWidgets.QTableWidgetItem(str(query.value(2))))

                    var.ui.tabServicios.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabServicios.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabServicios.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                    index += 1


        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error mostrar tabla ')
            msg.exec()
            print(error)

    def alta_servicio(newservicio):
        """

        Funcion que da de alta un nuevo servicio
        :return:  mensaje de alta correcta

        """
        try:
            query = QtSql.QSqlQuery()
            queryCli = QtSql.QSqlQuery()
            query.prepare('insert into servicios (codigo, concepto, preciounidad) '
                          'values (:codigo, :concepto, :preciounidad)')
            queryCli.prepare('select codigo from servicios where codigo = :codigo')
            queryCli.bindValue(':codigo', str(newservicio[0]))
            query.bindValue(':concepto', str(newservicio[1]))
            query.bindValue(':preciounidad', str(newservicio[2]))

            if query.exec():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Servicio dado de alta')
                msg.exec()

            Conexion.mostrar_tab_servicios(self=None)
            Conexion.carga_combo_facturas(self=None)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error alta servicio')
            msg.exec()
            print(error)


    def eliminar_servicio(Self):
        """

        Funcion que elimina un servicio
        :return:  mensaje de eliminacion correcta

        """
        try:
            codigo = Conexion.mostrar_servicio()
            query = QtSql.QSqlQuery()
            query.prepare('DELETE  from servicios where codigo = :codigo')
            query.bindValue(':codigo', codigo)
            print(codigo)
            if query.exec():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Producto eliminado con éxito')
                msg.exec()

            Conexion.mostrar_tab_servicios(self=None)
            Conexion.mostrar_tab_ventas()

        except Exception as error:
            print('Error en alta Productos: ', error)


    def modificar_servicio(self=None):
        """

        Funcion que modifica un servicio
        :return:  mensaje de modificacion correcta

        """
        try:
            codigo = var.ui.tabServicios.selectedItems()[0].data(0)
            concepto = var.ui.txtConcepto.text()
            precio = var.ui.txtPrecio.text()
            query = QtSql.QSqlQuery()
            query.prepare(
                'UPDATE servicios SET concepto= :concepto, preciounidad = :preciounidad WHERE codigo= :codigo')
            query.bindValue(':concepto', concepto)
            query.bindValue(':preciounidad', precio)
            query.bindValue(':codigo', codigo)

            if query.exec():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Cambios realizados con éxito !!')
                msg.exec()

            Conexion.mostrar_tab_servicios(self=None)
            Conexion.mostrar_tab_ventas(self=None)


        except Exception as error:
            print(error)

    def mostrar_servicio(self=None):
        """

        Funcion que muestra el servicio seleccionado en la tabla en las celdas
        :return:  codigo del servicio seleccionado
        """
        try:
            codigo = var.ui.tabServicios.selectedItems()[0].data(0)
            query = QtSql.QSqlQuery()
            query.prepare('select * from servicios where codigo = :codigo')  # Consulta en la base de datos
            query.bindValue(':codigo', codigo)
            if query.exec():
                while query.next():
                    var.ui.txtConcepto.setText(query.value(1))
                    var.ui.txtPrecio.setText(str(query.value(2)))
                    return query.value(0)
        except Exception as error:
            print(error)


    def one_servicio(codigo):
        """

        Funcion que devuelve un registro de la tabla servicios en una lista
        :return:  lista con los datos del registro

        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, concepto, preciounidad from servicios where codigo = :codigo')
            query.bindValue(':codigo', str(codigo))

            if query.exec():
                while query.next():
                    for i in range(3):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error carga servicio de tabla 2')
            msg.exec()
            print(error)

    # =================================================== FACTURAS ===================================================

    def mostrar_tab_ventas(self):
        """

        Funcion que muestra los datos de la tabla ventas en la tabla de la ventana principal
        :return:  tabla con los datos de la tabla ventas

        """
        try:
            index = 1
            codFac = var.ui.txtFactura.text()
            query = QtSql.QSqlQuery()
            query.prepare(
                'select idVentas, concepto, precio, unidades, subtotal from ventas  where codFac = :codFac ')
            query.bindValue(':codFac', codFac)

            if query.exec():
                while query.next():
                    var.ui.tabVentas.setRowCount(index + 1)
                    var.ui.tabVentas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(1))))
                    var.ui.tabVentas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(query.value(2))))
                    var.ui.tabVentas.setItem(index, 2, QtWidgets.QTableWidgetItem(str(query.value(3))))
                    var.ui.tabVentas.setItem(index, 3, QtWidgets.QTableWidgetItem(str(query.value(4))))

                    var.ui.tabVentas.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabVentas.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabVentas.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabVentas.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                    index += 1


        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error mostrar tabla ')
            msg.exec()
            print(error)

    def carga_combo_facturas(self=None):
        """

        Funcion que carga el combo de facturas con los datos de la tabla facturas
        :return:  combo con los datos de la tabla facturas

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select concepto from servicios order by concepto')
            if query.exec():
                while query.next():
                    var.cmbServicio.addItem(str(query.value(0)))


        except Exception as error:
            print(error)

    def cargar_precio(self=None):
        """

        Funcion que carga el precio del servicio seleccionado en el combo
        :return:  precio del servicio seleccionado

        """
        try:

            codigo = 0

            concepto = var.cmbServicio.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select codigo from servicios where concepto = :concepto')
            query.bindValue(':concepto', concepto)
            if query.exec():
                while query.next():
                    codigo = query.value(0)

            query1 = QtSql.QSqlQuery()
            query1.prepare('select preciounidad from servicios where codigo = :codigo')
            query1.bindValue(':codigo', int(codigo))

            if query1.exec():
                while query1.next():
                    precio = query1.value(0)
                    var.ui.tabVentas.setItem(0, 1, QtWidgets.QTableWidgetItem(str(precio)))

        except Exception as error:
            print(error)

    def add_venta(self):
        """

        Funcion que añade un registro a la tabla ventas
        :return:  registro añadido a la tabla ventas

        """
        try:
            Conexion.mostrar_tab_ventas(self)

            concepto = var.cmbServicio.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select codigo from servicios where concepto = :concepto')
            query.bindValue(':concepto', concepto)
            if query.exec():
                while query.next():
                    codigo = query.value(0)

            query1 = QtSql.QSqlQuery()
            query1.prepare('select preciounidad from servicios where codigo = :codigo')
            query1.bindValue(':codigo', int(codigo))

            index = 1
            if query1.exec():
                while query1.next():
                    precio = query1.value(0)
                    unidades = var.txtUnidades.text()
                    subtotal = float(precio) * float(unidades)
                    var.ui.tabVentas.setRowCount(index + 1)
                    var.ui.tabVentas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(concepto)))
                    var.ui.tabVentas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(precio)))
                    var.ui.tabVentas.setItem(index, 2, QtWidgets.QTableWidgetItem(str(unidades)))
                    var.ui.tabVentas.setItem(index, 3, QtWidgets.QTableWidgetItem(str(subtotal)))

                    var.ui.tabVentas.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabVentas.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabVentas.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabVentas.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                    query2 = QtSql.QSqlQuery()
                    query2.prepare(
                        'insert into ventas (concepto, precio, unidades, subtotal, codFac, codServ) values (  :concepto, :precio, :unidades, :subtotal, :codFac, :codServ)')

                    id = var.ui.txtFactura.text()
                    query2.bindValue(':concepto', concepto)
                    query2.bindValue(':precio', precio)
                    query2.bindValue(':unidades', unidades)
                    query2.bindValue(':subtotal', subtotal)
                    query2.bindValue(':codFac', str(id))
                    query2.bindValue(':codServ', codigo)


                    if query2.exec():
                        while query2.next():
                            print('Registro añadido')
                            Conexion.mostrar_tab_ventas(self)

                            index += 1

            Conexion.mostrar_tab_ventas(self)

            query3 = QtSql.QSqlQuery()
            query3.prepare('select sum(subtotal) from ventas')
            if query3.exec():
                while query3.next():
                    total = query3.value(0)
                    var.ui.lblSubtotal.setText(str(total))



        except Exception as error:
            print(error)

    def mostrar_tab_facturas(self):
        """

        Funcion que muestra los registros de la tabla facturas en la tabla de la pestaña facturas
        :return:  registros de la tabla facturas en la tabla de la pestaña facturas

        """

        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select * from facturas')
            if query.exec():
                while query.next():
                    var.ui.tabFacturas.setRowCount(index + 1)
                    var.ui.tabFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(0))))
                    var.ui.tabFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(query.value(3))))

                    var.ui.tabFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    index += 1

        except Exception as error:
            print(error)

    def alta_factura(self):
        """

        Funcion que da de alta una factura en la tabla facturas
        :return:  factura dada de alta en la tabla facturas

        """

        try:
            dni = var.ui.txtDniFac.text()
            fecha = var.ui.txtFechaFac.text()
            matricula = var.ui.txtMatriculaFac.text()


            query = QtSql.QSqlQuery()
            query.prepare('insert into facturas (dniCli, fechafac, matricula) values ( :dniCli, :fechafac, :matricula)')
            query.bindValue(':dniCli', dni)
            query.bindValue(':fechafac', fecha)
            query.bindValue(':matricula', matricula)

            if query.exec():
                    print('Factura dada de alta correctamente')

            Conexion.mostrar_tab_facturas(self=None)



        except Exception as error:
            print(error)

    def cargar_factura(self):
        """

        Funcion que carga los datos de la factura seleccionada en la tabla de la pestaña facturas en los campos de la pestaña facturas
        :return:  datos de la factura seleccionada en la tabla de la pestaña facturas en los campos de la pestaña facturas

        """

        try:

            fila = var.ui.tabFacturas.selectedItems()
            datos = [var.ui.txtFactura, var.ui.txtMatriculaFac]
            row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])

            query = QtSql.QSqlQuery()
            query.prepare('select idVenta, dniCli, fechafac, matricula from facturas where idVenta = :idVenta')
            query.bindValue(':idVenta', var.ui.txtFactura.text())
            if query.exec():
                while query.next():
                    var.ui.txtDniFac.setText(str(query.value(1)))
                    var.ui.txtFechaFac.setText(str(query.value(2)))
                    var.ui.txtMatriculaFac.setText(str(query.value(3)))
            # Vaciamos la tabla de ventas menos la primera fila
            for index in range(var.ui.tabVentas.rowCount() - 1, 0, -1):
                var.ui.tabVentas.removeRow(index)


            Conexion.mostrar_tab_ventas(self=None)

        except Exception as error:
            print(error)

    def limpia_factura(self):
        """

        Funcion que limpia los campos de la pestaña facturas
        :return:  campos de la pestaña facturas limpios

        """

        try:
            var.ui.txtDniFac.setText('')
            var.ui.txtMatriculaFac.setText('')
            var.ui.txtFechaFac.setText('')

        except Exception as error:
            print(error)

    def borrar_factura(self):
        """

        Funcion que borra una factura de la tabla facturas
        :return:  factura borrada de la tabla facturas
        
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from facturas where idVenta = :idVenta')
            query.bindValue(':idVenta', var.ui.txtFactura.text())
            if query.exec():
                print('Factura borrada correctamente')
            Conexion.mostrar_tab_facturas(self=None)
            Conexion.limpia_factura(self=None)
            Conexion.mostrar_tab_ventas(self=None)
            var.ui.lblSubtotal.setText('0')
        except Exception as error:
            print(error)

