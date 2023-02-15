from PyQt6 import QtWidgets
import conexion
import var


class Clientes():
    '''
    Validar DNI
    '''

    def validarDNI(dni):
        try:
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control
            return False
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al Validar DNI')
            msg.exec()
            print(error)

    '''
    DNI valido y letra mayus
    '''

    def mostrarValidoDNI(self=None):
        try:
            dni = var.ui.txtDni.text()
            if Clientes.validarDNI(dni):
                var.ui.lblValidarDni.setStyleSheet('color: green;')
                var.ui.lblValidarDni.setText('V')
                var.ui.txtDni.setText(dni.upper())
                var.ui.txtDni.setStyleSheet('background-color: #fff3b5;')

            else:
                var.ui.lblValidarDni.setStyleSheet('color: red;')
                var.ui.lblValidarDni.setText('X')
                var.ui.txtDni.setText(dni.upper())
                var.ui.txtDni.setStyleSheet('background-color: pink;')

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error DNI valido')
            msg.exec()
            print(error)

    '''
    Seleccionar motor
    '''

    def selMotor(self=None):
        try:
            var.motor = (var.ui.rbtGasolina, var.ui.rbtDiesel, var.ui.rbtHibrido, var.ui.rbtElectrico)
            for i in var.motor:
                i.toggled.connect(Clientes.checkMotor)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error seleccionar motor')
            msg.exec()
            print(error)

    '''
    Validar motor seleccionado
    '''

    def checkMotor(self=None):
        try:
            if var.ui.rbtGasolina.isChecked():
                motor = 'Gasolina'
            elif var.ui.rbtDiesel.isChecked():
                motor = 'Diesel'
            elif var.ui.rbtHibrido.isChecked():
                motor = 'Hibrido'
            elif var.ui.rbtElectrico.isChecked():
                motor = 'Electrico'
            else:
                pass
            return motor

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error validar motor')
            msg.exec()
            print(error)

    '''
    Guardar clinte
    '''

    def guardaCli(self=None):
        try:
            newcli = []
            newcar = []
            pagos = []

            car = [var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo]
            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtFechaltacli, var.ui.txtDirCli]

            for i in cliente:
                newcli.append(i.text())
            for i in car:
                newcar.append(i.text())

            prov = var.ui.cmbProcli.currentText()
            muni = var.ui.cmbMunicli.currentText()
            motor = Clientes.checkMotor()

            newcli.append(prov)
            newcli.append(muni)
            newcar.append(motor)

            if var.ui.chkEfec.isChecked():
                pagos.append('Efectivo')
            if var.ui.chkTrans.isChecked():
                pagos.append('Transeferencia')
            if var.ui.chkTar.isChecked():
                pagos.append('Tarjeta')

            pagos = set(pagos)
            newcli.append('; '.join(pagos))

            conexion.Conexion.altaCli(newcli, newcar)
            print(newcli)
            print(newcar)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error guardar Cliente')
            msg.exec()
            print(error)

    '''
    Cargar fecha
    '''

    def cargaFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFechaltacli.setText(str(data))
            var.dlgcalendar.hide()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error cargar Fecha Alta')
            msg.exec()
            print(error)

    '''
    Limpiar celdas
    '''

    def limpiaCli(self=None):
        try:
            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtDirCli, var.ui.txtFechaltacli, var.ui.txtMatricula,
                       var.ui.txtMarca, var.ui.txtModelo]
            for i in cliente:
                i.setText('')

            btns = [var.ui.chkEfec, var.ui.chkTar, var.ui.chkTrans]

            for btn in btns:
                btn.setChecked(False)

            var.ui.cmbProcli.setCurrentText(str(''))
            var.ui.cmbMunicli.setCurrentText(str(''))

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error limpiar campos')
            msg.exec()
            print(error)

    '''
    Caragar cliente seleccionado en tabla en las celdas
    '''

    def cargaCliente(self=None):
        try:
            Clientes.limpiaCli()
            fila = var.ui.tabClientes.selectedItems()
            datos = [var.ui.txtDni, var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo]
            row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])

            if row[4] == 'Diesel':
                var.ui.rbtDiesel.setChecked(True)
            elif row[4] == 'Gasolina':
                var.ui.rbtGasolina.setChecked(True)
            elif row[4] == 'Hibrido':
                var.ui.rbtHibrido.setChecked(True)
            elif row[4] == 'Electrico':
                var.ui.rbtElectrico.setChecked(True)

            registro = conexion.Conexion.oneCli(row[0])

            var.ui.txtNombre.setText(registro[0])
            var.ui.txtFechaltacli.setText(registro[1])
            var.ui.txtDirCli.setText(registro[2])
            var.ui.cmbProcli.setCurrentText(registro[3])
            var.ui.cmbMunicli.setCurrentText(registro[4])

            if 'Efectivo' in registro[5]:
                var.ui.chkEfec.setChecked(True)
            if 'Transferencia' in registro[5]:
                var.ui.chkTrans.setChecked(True)
            if 'Tarjeta' in registro[5]:
                var.ui.chkTar.setChecked(True)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error carga cliente de tabla2')
            msg.exec()
            print(error)

    '''
    Borrar cliente
    '''

    def borraCli(self):
        try:
            dni = var.ui.txtDni.text()
            conexion.Conexion.borrarCli(dni)
            conexion.Conexion.mostrarTabcarcli(self)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error borrar cliente')
            msg.exec()
            print(error)

    '''
    Modificar cliente
    '''

    def modifCli(self):
        try:
            modcar = []
            modcli = []
            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtFechaltacli, var.ui.txtDirCli]

            for i in cliente:
                modcli.append(i.text())

            prov = var.ui.cmbProcli.currentText()
            modcli.append(prov)

            muni = var.ui.cmbMunicli.currentText()
            modcli.append(muni)

            pagos = []

            if var.ui.chkEfec.isChecked():
                pagos.append('Efectivo')
            if var.ui.chkTrans.isChecked():
                pagos.append('Transeferencia')
            if var.ui.chkTar.isChecked():
                pagos.append('Tarjeta')

            pagos = set(pagos)
            modcli.append('; '.join(pagos))

            car = [var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo]
            for i in car:
                modcar.append(i.text())
            motor = Clientes.checkMotor()
            modcar.append(motor)

            conexion.Conexion.modificaCli(modcli, modcar)
            conexion.Conexion.mostrarTabcarcli(self)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error modificar cliente')
            msg.exec()
            print(error)
