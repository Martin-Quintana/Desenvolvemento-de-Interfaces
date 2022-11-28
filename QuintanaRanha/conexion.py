import datetime

from PyQt6 import QtSql
from datetime import datetime
import clientes
import var
from ventMain import *


class Conexion():


    '''
    Metodo conexion, para conectar la base de datos con la aplicacion
    '''
    def conexion(self=None):
        filedb = 'BBDD.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filedb)
        var.bbdd = 'BBDD.sqlite'
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos',
                                           'Conexion no establecida.\n', 'Haga click para cerrar',
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False
        else:
            print('Conexion establecida')
            return True


    '''
    Metodo que sirve para cargar la provincia de la tabla Provincias de la base de datos
    '''
    def cargarProvincia(self=None):
        try:
            var.ui.cmbProcli.clear()
            # Creamos una variable para la consulta
            query = QtSql.QSqlQuery()
            # Escribimos la consulta
            query.prepare('select provincia from provincias')
            # Ejecutamos la consulta
            if query.exec():
                var.ui.cmbProcli.addItem('')
                while query.next():
                    var.ui.cmbProcli.addItem(query.value(0))

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al cargar las provincias')
            msg.exec()


    '''
    Metodo que sirve para seleccionar el municipio dependiendo de que provincia haya sido seleccionada
    '''
    def selMuni(self=None):
        try:
            # query significa consulta :)
            id = 0
            var.ui.cmbMunicli.clear()
            prov = var.ui.cmbProcli.currentText()
            # Creamos una variable para la consulta
            query = QtSql.QSqlQuery()
            # Escribimos la consulta
            query.prepare('select id from provincias where provincia = :prov')
            # Relacionar un elemento de la BBDD con uno de Python
            query.bindValue(':prov', prov)
            # Ejecutamos la consulta
            if query.exec():
                while query.next():
                    id = query.value(0)
            # Creamos una variable para la consulta
            query1 = QtSql.QSqlQuery()
            # Escribimos la consulta
            query1.prepare('select municipio from municipios where provincia_id = :id')
            # Relacionar un elemento de la BBDD con uno de Python
            query1.bindValue(':id', int(id))
            # Ejecutamos la consulta
            if query1.exec():
                var.ui.cmbMunicli.addItem('')
                while query1.next():
                    var.ui.cmbMunicli.addItem(query1.value(0))


        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error en la carga de Municipios')
            msg.exec()


    '''
    Metodo que sirve para dar de alta a un Cliente en la base de datos
    '''
    def altaCli(newcli, newcar):
        try:
            dnirepe = ''

            # Creamos una variable para la consulta
            query = QtSql.QSqlQuery()
            # Creamos una variable para la consulta
            queryCli = QtSql.QSqlQuery()
            # Escribimos la consulta
            query.prepare('insert into clientes (dni, nombre, alta, direccion, provincia, municipio, pago) '
                          'values (:dni, :nombre, :alta, :direccion, :provincia, :municipio, :pago)')
            # Escribimos la consulta
            queryCli.prepare('select dni from clientes where dni = :dni')

            # Relacionar un elemento de la BBDD con uno de Python
            queryCli.bindValue(':dni', str(newcli[0]))
            query.bindValue(':dni', str(newcli[0]))
            query.bindValue(':nombre', str(newcli[1]))
            query.bindValue(':alta', str(newcli[2]))
            query.bindValue(':direccion', str(newcli[3]))
            query.bindValue(':provincia', str(newcli[4]))
            query.bindValue(':municipio', str(newcli[5]))
            query.bindValue(':pago', str(newcli[6]))

            # Ejecutamos la consulta
            if query.exec():
                pass
            # Creamos una variable para la consulta
            query1 = QtSql.QSqlQuery()
            # Escribimos la consulta
            query1.prepare('insert into coches(matricula, dnicli, marca, modelo, motor) '
                           'values (:matricula, :dnicli, :marca, :modelo, :motor)')
            # Relacionar un elemento de la BBDD con uno de Python
            query1.bindValue(':matricula', str(newcar[0]))
            query1.bindValue(':dnicli', str(newcli[0]))
            query1.bindValue(':marca', str(newcar[1]))
            query1.bindValue(':modelo', str(newcar[2]))
            query1.bindValue(':motor', str(newcar[3]))

            # Ejecutamos la consulta    Y mostramos un mensaje donde el decimos que el coche ha sido dado de Alta
            if query1.exec():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('COCHE DADO DE ALTA')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText(query1.lastError().text())
                msg.exec()
            Conexion.mostrarTabcarcli(self = None)
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error en el alta de Cliente')
            msg.exec()

    '''
    Metodo que sirve para mostrar los datos del Cliente en la tabla
    '''
    def mostrarTabcarcli(self):
        try:
            index = 0
            # Creamos una variable para la consulta
            query = QtSql.QSqlQuery()
            # Escribimos la consulta
            query.prepare('select matricula, dnicli, marca, modelo, motor from coches where fechabajacar is null order by marca, modelo')
            if query.exec():
                while query.next():
                    var.ui.tabClientes.setRowCount(index + 1)  # Creamos la fila
                    #Centrar la parte de arriba de la tabla
                    var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(1))))
                    var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(query.value(0))))
                    var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(query.value(2))))
                    var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(query.value(3))))
                    var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(query.value(4))))

                    #Centrar el texto de las celdas de cada columna
                    var.ui.tabClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                    index += 1
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al mostrar la Tabla ' )
            msg.exec()


    '''
    Metodo que sirve para visualizar los datos del Cliente cuando seleccionas los datos de su Coche en la tabla
    '''
    def oneCli(dni):
        try:

            registro = []
            # Creamos una variable para la consulta
            query = QtSql.QSqlQuery()
            # Escribimos la consulta
            query.prepare('select nombre, alta, direccion, provincia, municipio, pago from clientes where dni = :dni')
            # Relacionar un elemento de la BBDD con uno de Python
            query.bindValue(':dni', str(dni))
            # Ejecutamos la consulta
            if query.exec():
                while query.next():
                    for i in range(6):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error oneCli')
            msg.exec()


    '''
    Metodo que sirve para dar de alta en la base de datos a traves de un Excel nuevos Coches
    '''
    def altaExcelCoche(new):
        try:
            #Creamos una variable para la consulta
            query1 = QtSql.QSqlQuery()
            #Escribimos la consulta
            query1.prepare('insert into coches(matricula, dnicli, marca, modelo, motor, fechabajacar) '
                           'values (:matricula, :dnicli, :marca, :modelo, :motor, :fechabajacar)')
            #Relacionar un elemento de la BBDD con uno de Python
            query1.bindValue(':matricula', str(new[0]))
            query1.bindValue(':dnicli', str(new[1]))
            query1.bindValue(':marca', str(new[2]))
            query1.bindValue(':modelo', str(new[3]))
            query1.bindValue(':motor', str(new[4]))
            query1.bindValue(':fechabajacar', str(new[5]))
            #Ejecutamos la consulta
            if query1.exec():
                pass


        except Exception as error:
            #Ventana de Error
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al dar de alta el Excel del Coche')
            msg.exec()


    '''
    Metodo que sirve para comprobar que todos los campos son validos/io estan vacios
    '''
    def comprobarCamposValidos(self=None):
        try:
            #Guardamos el DNI en una variable
            dni = var.ui.txtDni.text()
            #Comprobamos que el DNI es correcto si lo es comprobamos que el resto de los campos no estan vacios y
            # se guarda el Cliente
            if clientes.Clientes.validarDNI(dni) \
                    and len(var.ui.txtNombre.text()) > 0 and len(var.ui.txtDirCli.text()) > 0 \
                    and len(var.ui.txtMatricula.text()) > 0 and len(var.ui.txtMarca.text()) > 0 \
                    and len(var.ui.txtModelo.text()) > 0 and len(var.ui.cmbProcli.currentText()) > 0 \
                    and len(var.ui.cmbMunicli.currentText()) > 0 and len(var.ui.txtFechaltacli.text()) > 0:
                clientes.Clientes.guardaCli()
            #Salta una Ventana de error que dice 'Error al Cargar Cliente'
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('ERROR AL CARGAR CLIENTE')
                msg.exec()
                return False
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al comprobar los Datos')
            msg.exec()
            print(error)


    '''
    Metodo que sirve para borrar CLiente
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
            msg.setText('Error al borra Cliente en Conexion')
            msg.exec()
            print(error)

    '''
    Metodo que sirve para modificar el Cliente en la base de datos
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
            # Relacionar un elemento de la BBDD con uno de Python
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

            Conexion.mostrarTabcarcli(self= None)


        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al modificar Cliente en Conexion')
            msg.exec()
            print(error)








