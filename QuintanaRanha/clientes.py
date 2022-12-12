from PyQt6 import QtWidgets

import conexion
import var


# Clase clientes, que tiene meetodos que hace algo con los datos de los clientes
class Clientes():
    '''
    Metodo para la validacion de DNI
    :return: boolean
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
    Metodo para mostrar que la validacion del DNI es correcta y poner la letra del DNI en mayusculas
    Anhadimos algun color para mejorar la usabilidad
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
            msg.setText('Error al error al mostrar color y validez del DNI')
            msg.exec()
            print(error)

    '''
    Metodo para seleccionar el tipo de motor
    '''

    def selMotor(self=None):
        try:
            # Crea una tupla con los tipos de motor para comprobar cual es
            var.motor = (var.ui.rbtGasolina, var.ui.rbtDiesel, var.ui.rbtHibrido, var.ui.rbtElectrico)
            for i in var.motor:
                i.toggled.connect(Clientes.checkMotor)
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error seleccion de motor')
            msg.exec()
            print(error)

    '''
    Metodo para chequear que el motor ha sido seleccionado correctamente
    '''

    def checkMotor(self=None):
        try:
            # Comprueba que motor a sido seleccionado
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
            msg.setText('Error check motor')
            msg.exec()
            print(error)

    '''
    Metodo que sirve para guardar el cliente en la base de datos en base a lo que escribimos en la interfaz
    '''

    def guardaCli(self=None):
        try:
            # Creamos una lista de: Clientes nuevos, coches nuevos y pagos
            newcli = []
            newcar = []
            pagos = []

            # Creamos la lista coche con sus respectivos campos
            car = [var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo]

            #Creamos la lista Cliente con sus respectivos campos
            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtFechaltacli, var.ui.txtDirCli]


            for i in cliente:
                newcli.append(i.text())
            for i in car:
                newcar.append(i.text())

            # Cogemos la provincia el municipio y el tipo de motor del Coche
            prov = var.ui.cmbProcli.currentText()
            muni = var.ui.cmbMunicli.currentText()
            motor = Clientes.checkMotor()

            # Anhadimos cada uno a su respectiva lista
            newcli.append(prov)
            newcli.append(muni)
            newcar.append(motor)


            # Comprobamos el tipo de Pago que ha seleccionado
            if var.ui.chkEfec.isChecked():
                pagos.append('Efectivo')
            if var.ui.chkTrans.isChecked():
                pagos.append('Transeferencia')
            if var.ui.chkTar.isChecked():
                pagos.append('Tarjeta')

            pagos = set(pagos)  # evita duplicados
            newcli.append('; '.join(pagos))

            conexion.Conexion.altaCli(newcli, newcar)
            print(newcli)
            print(newcar)
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al cargar Cliente')
            msg.exec()
            print(error)

    '''
    Metodo que sirve para cargar la fecha a traves de la ventana de calendario
    '''

    def cargaFecha(qDate):
        try:
            # Creamos tuplas de Fecha
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            # Escribimos el label de la Fecha de Alta
            var.ui.txtFechaltacli.setText(str(data))
            # Escondemos la ventana del calendario
            var.dlgcalendar.hide()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al cargar Fecha alta del Cliente')
            msg.exec()
            print(error)

    '''
    Metodo que sirve para limpiar las celdas de la informacion de los clientes
    '''

    def limpiaCli(self=None):
        try:
            # Creamos una lista con los campos del cliente
            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtDirCli, var.ui.txtFechaltacli,
                       var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo]
            # Vaciamos esa lista
            for i in cliente:
                i.setText('')
            # Creamos una lista con los botones de tipo de pago
            btns = [var.ui.chkEfec, var.ui.chkTar, var.ui.chkTrans]
            # Le decimos que los botones no esta clicados
            for btn in btns:
                btn.setChecked(False)
            # Vaciamos las comboBox de la Provincia y del Municipio
            var.ui.cmbProcli.setCurrentText(str(''))
            var.ui.cmbMunicli.setCurrentText(str(''))


        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al limpiar los campos del Cliente')
            msg.exec()
            print(error)


    '''
    Metodo que sirve oara cargar el cliente de la tabla en los labels
    '''
    def cargaCliente(self=None):
        try:
            #Primero limpiamos los campos de los Clientes para que no haya ningun tipo de problema
            Clientes.limpiaCli()
            fila = var.ui.tabClientes.selectedItems()  #Recoge todo lo que hay en la fila seleccionada de la tabla
            datos = [var.ui.txtDni, var.ui.txtMatricula, var.ui.txtMarca,
                     var.ui.txtModelo]  # Son los datos que hay en la tabla
            row = [dato.text() for dato in fila]  # Creas un listado con los datos

            for i, dato in enumerate(datos):
                dato.setText(row[i])

            #Checkeamos los rbtMotor dependiendo de su tipo de motor
            if row[4] == 'Diesel':
                var.ui.rbtDiesel.setChecked(True)
            elif row[4] == 'Gasolina':
                var.ui.rbtGasolina.setChecked(True)
            elif row[4] == 'Hibrido':
                var.ui.rbtHibrido.setChecked(True)
            elif row[4] == 'Electrico':
                var.ui.rbtElectrico.setChecked(True)

            registro = conexion.Conexion.oneCli(row[0])#registro del cliente

            # Cargamos el todas los campos del Cliente
            var.ui.txtNombre.setText(registro[0])
            var.ui.txtFechaltacli.setText(registro[1])
            var.ui.txtDirCli.setText(registro[2])
            var.ui.cmbProcli.setCurrentText(registro[3])
            var.ui.cmbMunicli.setCurrentText(registro[4])

            # Comprobante de que check box esta clicada y cargamos la que esta cargada
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
            msg.setText('Error al cargar Cliente de la tabla')
            msg.exec()
            print(error)

    '''
    Metodo que sirve para borrar el cliente
    '''
    def borraCli (self):
        try:
            dni = var.ui.txtDni.text()
            conexion.Conexion.borrarCli(dni)
            conexion.Conexion.mostrarTabcarcli(self)
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al borrar el Cliente y sus Coches')
            msg.exec()
            print(error)


    '''
    Metodo que sirve para mdoificar clientes
    '''
    def modifCli(self):
        try:
            modcar = []
            modcli = []
            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtFechaltacli,var.ui.txtDirCli]

            for i in cliente:
                modcli.append(i.text())
            # Provincia
            prov = var.ui.cmbProcli.currentText()
            modcli.append(prov)
            # Municipio
            muni = var.ui.cmbMunicli.currentText()
            modcli.append(muni)

            # Pagos
            pagos = []
            if var.ui.chkEfec.isChecked():
                pagos.append('Efectivo')
            if var.ui.chkTrans.isChecked():
                pagos.append('Transeferencia')
            if var.ui.chkTar.isChecked():
                pagos.append('Tarjeta')
            pagos = set(pagos) # Evita duplicados
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
            msg.setText('Error al modificar el Cliente')
            msg.exec()
            print(error)
