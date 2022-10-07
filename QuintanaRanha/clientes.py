from PyQt6 import QtWidgets
import var

class Clientes():


    '''
    Metodo para validar el DNI si existe o no
    '''
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

    '''
    Metodo que sirve para mostrar si el DNI es valido o no
    '''
    def mostrarValidoDNI(self = None):
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


    '''
    Metodo para saber que motor has selecionado
    '''
    def selMotor(self=None):
        try:
            var.motor = (var.ui.rbtGasolina, var.ui.rbtDiesel, var.ui.rbtHibrido, var.ui.rbtElectrico)
            for i in var.motor:
                i.toggled.connect(Clientes.checkMotor)

        except Exception as error:
            print('Error selecion motor: ', error)

    '''
    Metodo para checkear que motor has cogido
    '''
    def checkMotor(self=None):
        try:
            if var.ui.rbtGasolina.isChecked():
                motor ='Gasolina'
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
            print('Error check motor: ', error)


    '''
    Metodo para cargar los clientes 
    '''
    def guardaCli(self = None):
        try:
            newcli = []
            cliente = [var.ui.txtDni, var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo]
            for i in cliente:
                newcli.append(i.text())

            motor = Clientes.checkMotor()
            newcli.append(motor)
            row = 0 #Fila
            colum = 0 #Columna

            var.ui.tabClientes.insertRow(row)
            for resgistro in newcli:
                cell = QtWidgets.QTableWidgetItem(resgistro) #Cell = celda
                var.ui.tabClientes.setItem(row, colum, cell)
                colum += 1

        except Exception as error:
            print('Error en carga cliente: ', error)