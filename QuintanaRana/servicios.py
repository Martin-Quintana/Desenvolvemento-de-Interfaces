from PyQt6 import QtWidgets
import conexion
import var

class Servicios():
    def guarda_servicio(self=None):
        try:
            newservicio = []

            servicio = [var.ui.txtCodigo, var.ui.txtConcepto, var.ui.txtPrecio]

            for i in servicio:
                newservicio.append(i.text())

            conexion.Conexion.alta_servicio(newservicio)
            print(newservicio)


        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error guardar Cliente')
            msg.exec()
            print(error)

    '''
    Limpiar celdas
    '''

    def limpia_servicio(self=None):
        try:
            servicio = [var.ui.txtCodigo, var.ui.txtConcepto, var.ui.txtPrecio]
            for i in servicio:
                i.setText('')

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error limpiar campos')
            msg.exec()
            print(error)

    '''
    Caragar servicio seleccionado en tabla en las celdas
    '''

    def carga_servicio(self=None):
        try:
            Servicios.limpia_servicio()
            fila = var.ui.tabServicios.selectedItems()
            datos = [var.ui.txtCodigo, var.ui.txtConcepto, var.ui.txtPrecio]
            row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])

            registro = conexion.Conexion.one_servicio(row[0])

            var.ui.txtCodigo.setText(registro[0])
            var.ui.txtConcepto.setText(registro[1])
            var.ui.txtPrecio.setText(registro[2])


        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error carga servicio de tabla')
            msg.exec()
            print(error)

    '''
    Borrar servicio
    '''

    def borra_servicio(self):
        try:
            codigo = var.ui.txtCodigo.text()
            conexion.Conexion.eliminar_servicio(codigo)
            conexion.Conexion.mostrar_tab_servicios(self)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error borrar servicio')
            msg.exec()
            print(error)

    '''
    Modificar servicio
    '''

    def modificar_servicio(self):
        try:
            modservicio = []
            servicio = [var.ui.txtCodigo, var.ui.txtConcepto, var.ui.txtPrecio]

            for i in servicio:
                modservicio.append(i.text())

            conexion.Conexion.modificar_servicio(modservicio)
            conexion.Conexion.mostrar_tab_servicios(self)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error modificar servicio')
            msg.exec()
            print(error)


