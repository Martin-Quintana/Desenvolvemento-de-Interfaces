import var

class Clientes():
    def validarDNI(dni):
        '''
            Modulo para la validacion del DNI
        :return: booleano
        '''
        try:
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()
            if len(dni) == 0:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni)%23] == dig_control
            return False

        except Exception as error:
            print('Error validar DNI: ', error)

    def mostrarValidoDNI(self):
        try:
            dni = var.ui.txtDni.setText
            if Clientes.validarDNI(dni):
                var.ui.lblValidarDni.setStyleSheet('QLabel: {color: green)')
                var.ui.lblValidarDni.setText('V')
                var.ui.txtDni.setText(dni.upper())
            else:
                var.ui.lblValidarDni.setStyleSheet('QLabel: {color: red)')
                var.ui.lblValidarDni.setText('X')
                var.ui.txtDni.setText(dni.upper())

        except Exception as error:
            print('Error mostrar marcado validez DNI: ', error)