from PyQt6 import QtWidgets

import conexion
import var


class Clientes():
    def validarDNI(dni):
        '''
        Modulo para la validacion de DNI
        :return: boolean
        '''
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
            print('Error validar DNI: ', error)

    def mostrarValidoDNI(self=None):
        try:
            dni = var.ui.txtDni.text()
            if Clientes.validarDNI(dni):
                var.ui.lblValidarDni.setStyleSheet('color: green;')
                var.ui.lblValidarDni.setText('V')
                var.ui.txtDni.setText(dni.upper())
                var.ui.txtDni.setStyleSheet('background-color: white;')
            else:
                var.ui.lblValidarDni.setStyleSheet('color: red;')
                var.ui.lblValidarDni.setText('X')
                var.ui.txtDni.setText(dni.upper())
                var.ui.txtDni.setStyleSheet('background-color: pink;')
        except Exception as error:
            print('Error mostrar marcado DNI: ', error)

    def selMotor(self=None):
        try:
            var.motor = (var.ui.rbtGasolina, var.ui.rbtDiesel, var.ui.rbtHibrido, var.ui.rbtElectrico)
            for i in var.motor:
                i.toggled.connect(Clientes.checkMotor)
        except Exception as error:
            print('Error selecion motor', error)

    def checkMotor(self = None):
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
            print('Error check motor', error)


    def guardaCli(self = None):
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

            if var.ui.chkEfectivo.isChecked():
                pagos.append('Efectivo')

            if var.ui.chkTransferencia.isChecked():
                pagos.append('Transeferencia')

            pagos = set(pagos)  # evita duplicados
            newcli.append('; '.join(pagos))

            conexion.Conexion.altaCli(newcli, newcar)
            print(newcli)
            print(newcar)









            '''
            row = 0
            column = 0
            var.ui.tabClientes.insertRow(row)
            for registro in newcli:
                cell = QtWidgets.QTableWidgetItem(registro)
                var.ui.tabClientes.setItem(row, column, cell)
                column += 1
            '''
        except Exception as error:
            print("Error en carga clientes", error)

    def cargaFecha (qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFechaltacli.setText(str(data))
            var.dlgcalendar.hide()

        except Exception as error:
            print('Error al cargar Fecha alta Cliente', error)


    def limpiaCli (self = None):
        try:
            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtDirCli, var.ui.txtFechaltacli,
                       var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo]
            for i in cliente:
                i.setText('')

            for i in var.ui.btnGroupPago.buttons():
                i.setChecked(False)
            conexion.Conexion.cargarProvincia(self)
        except Exception as error:
            print('Error al limpiar bien', error)