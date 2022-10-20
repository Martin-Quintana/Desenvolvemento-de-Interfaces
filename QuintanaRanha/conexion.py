from PyQt6 import QtWidgets, QtSql

import var, sys
from ventMain import *
class Conexion():

    def conexion (self = None):
        filedb = 'BBDD.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filedb)
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos',
                                           'Conexion no establecida.\n', 'Haga click para cerrar',
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False
        else:
            print('Conexion establecida')
            return True

    def cargarProvincia (self = None):
        try:
            var.ui.cmbProcli.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec():
                var.ui.cmbProcli.addItem('')
                while query.next():
                    var.ui.cmbProcli.addItem(query.value(0))

        except Exception as error:
            print('Error cargar provincias', error)

    def selMuni(self = None):
        try:
            #query significa consulta :)
            id = 0
            var.ui.cmbMunicli.clear()
            prov = var.ui.cmbProcli.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select id from provincias where provincia = :prov') #Consulta en la base de datos
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
            print('Error carga de municipios', error)

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

        except Exception as error:
            print('Error en alta cliente: ', error)
