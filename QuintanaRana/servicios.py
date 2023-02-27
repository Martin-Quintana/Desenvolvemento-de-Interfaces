from PyQt6 import QtWidgets
import conexion
import var

class Servicios():
    def guardaServicio(self=None):
        try:
            newservicio = []

            servicio = [var.ui.txtCodigo, var.ui.txtConcepto, var.ui.txtPrecio]

            for i in servicio:
                newservicio.append(i.text())

            conexion.Conexion.altaServicio(newservicio)
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

    def limpiaServicio(self=None):
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

    def cargaServicio(self=None):
        try:
            Servicios.limpiaServicio()
            fila = var.ui.tabServicios.selectedItems()
            datos = [var.ui.txtCodigo, var.ui.txtConcepto, var.ui.txtPrecio]
            row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])

            registro = conexion.Conexion.oneServicio(row[0])

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

    def borraServicio(self):
        try:
            codigo = var.ui.txtCodigo.text()
            conexion.Conexion.delServicio(codigo)
            conexion.Conexion.mostrarTabservicios(self)

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

    def modifServicio(self):
        try:
            modservicio = []
            servicio = [var.ui.txtCodigo, var.ui.txtConcepto, var.ui.txtPrecio]

            for i in servicio:
                modservicio.append(i.text())

            conexion.Conexion.modServicio(modservicio)
            conexion.Conexion.mostrarTabservicios(self)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error modificar servicio')
            msg.exec()
            print(error)


