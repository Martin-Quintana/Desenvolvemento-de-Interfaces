import datetime

from PyQt6 import QtSql
from datetime import datetime
import clientes
import var
from ventMain import *


class Conexion():
    '''
    Conectar con bbdd
    '''

    def conexion(self=None):
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

    '''
    Cargar provincias
    '''

    def cargarProvincia(self=None):
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

    '''
    Seleccionar municipio segun provincia
    '''

    def selMuni(self=None):
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

    '''
    Alta en la bbdd de cliente
    '''

    def altaCli(newcli, newcar):
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
            Conexion.mostrarTabcarcli(self=None)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error alta cliente')
            msg.exec()
            print(error)

    '''
    Mostrar clientes en la tabla
    '''

    def mostrarTabcarcli(self):
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

    '''
    Caragar cliente seleccionado en tabla en las celdas
    '''

    def oneCli(dni):
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

    '''
    Alta coches con Excel
    '''

    def altaExcelCoche(new):
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

    '''
    Campos validos
    '''

    def comprobarCamposValidos(self=None):
        try:
            dni = var.ui.txtDni.text()

            if clientes.Clientes.validarDNI(dni) \
                    and len(var.ui.txtNombre.text()) > 0 and len(var.ui.txtDirCli.text()) > 0 \
                    and len(var.ui.txtMatricula.text()) > 0 and len(var.ui.txtMarca.text()) > 0 \
                    and len(var.ui.txtModelo.text()) > 0 and len(var.ui.cmbProcli.currentText()) > 0 \
                    and len(var.ui.cmbMunicli.currentText()) > 0 and len(var.ui.txtFechaltacli.text()) > 0:
                clientes.Clientes.guardaCli()

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

    '''
    Borrar cliente en la bbdd
    '''

    def borrarCli(dni):
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

    '''
    Modificar cliente en la bbdd
    '''

    def modificaCli(modcli, modcar):
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

            Conexion.mostrarTabcarcli(self=None)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error modificar cliente bbdd')
            msg.exec()
            print(error)

    '''
    Buscar coche por matricula
    '''

    def buscaCoche(self):
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

    '''
    Mostrar tabla servicios
    '''

    def mostrarTabservicios(self):
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

    '''
    Dar de alta un servicio
    '''

    def altaServicio(newservicio):
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

            Conexion.mostrarTabservicios(self=None)
            Conexion.cargaComboFacturas(self=None)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error alta servicio')
            msg.exec()
            print(error)

    '''
    Eliminar un servicio
    '''

    def delServicio(Self):
        try:
            codigo = Conexion.mostrarServicio()
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

            Conexion.mostrarTabservicios(self=None)
            Conexion.mostrarTabVentas()

        except Exception as error:
            print('Error en alta Productos: ', error)

    '''
    Modificar un servicio
    '''

    def modServicio(self=None):
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

            Conexion.mostrarTabservicios(self=None)
            Conexion.mostrarTabVentas(self=None)


        except Exception as error:
            print(error)

    '''
    Mostrar servicio seleccionado en la tabla
    '''

    def mostrarServicio(self=None):
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

    '''
    Caragar servicio seleccionado en tabla en las celdas
    '''

    def oneServicio(codigo):
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

    def mostrarTabVentas(idVentas):
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare(
                'select concepto, precio, unidades, subtotal from ventas order by concepto ')
            query.bindValue(':idVentas', str(idVentas))

            if query.exec():
                while query.next():
                    var.ui.tabVentas.setRowCount(index + 1)
                    var.ui.tabVentas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(0))))
                    var.ui.tabVentas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(query.value(1))))
                    var.ui.tabVentas.setItem(index, 2, QtWidgets.QTableWidgetItem(str(query.value(2))))
                    var.ui.tabVentas.setItem(index, 3, QtWidgets.QTableWidgetItem(str(query.value(3))))

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

    def cargaComboFacturas(self=None):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select concepto from servicios order by concepto')
            if query.exec():
                while query.next():
                    var.cmbServicio.addItem(str(query.value(0)))


        except Exception as error:
            print(error)

    def cargaPrecio(self=None):
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


            # concepto = var.cmbServicio.currentText()
            # query = QtSql.QSqlQuery()
            # query.prepare('select preciounidad from servicios where concepto = :concepto')
            # query.bindValue(':concepto', concepto)
            # if query.exec():
            #     while query.next():
            #
            #         var.ui.tabVentas.setItem(0,1, QtWidgets.QTableWidgetItem(str(query.value(0))))
            #         return query.value(0)


        except Exception as error:
            print(error)

    # def add_Venta(self):
    #     try:
    #         index = 1
    #         var.cmbServicio = QtWidgets.QComboBox()
    #         var.txtUnidades = QtWidgets.QLineEdit()
    #         var.ui.tabVentas.setRowCount(index + 1)
    #         var.ui.tabVentas.setCellWidget(index, 0, var.cmbServicio)
    #         var.ui.tabVentas.setCellWidget(index, 2, var.txtUnidades)
    #         index += 1
    #
    #         Conexion.cargaComboFacturas()
    #         Conexion.cargaPrecio()
    #
    #
    #
    #     except Exception as error:
    #         print(error)
