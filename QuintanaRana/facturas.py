from PyQt6 import QtWidgets, QtCore
import conexion
import var


class Facturas():
    def carga_linea_venta(index):
        """

        Carga una linea de venta en la tabla de ventas
        :param index:
        :return:  None

        """
        try:
            index = 0
            var.cmbServicio = QtWidgets.QComboBox()
            var.txtUnidades = QtWidgets.QLineEdit()
            var.ui.tabVentas.setRowCount(index + 1)
            var.ui.tabVentas.setCellWidget(index, 0, var.cmbServicio)
            var.ui.tabVentas.setCellWidget(index, 2, var.txtUnidades)
            index += 1

            conexion.Conexion.carga_combo_facturas()
            conexion.Conexion.cargar_precio()
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al cargar linea ventas ')
            msg.exec()
            print(error)

    def limpiar_factura(self):
        """

        Limpia los campos de la ventana de facturas
        :return None

        """
        try:
            var.ui.txtFactura.setText('')
            var.ui.txtDniFac.setText('')
            var.ui.txtMatriculaFac.setText('')
            var.ui.txtFechaFac.setText('')
            var.ui.txtDniFac.setText('')

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al limpiar factura ')
            msg.exec()
            print(error)



    def cargar_cliente(self):
        """

        Carga los datos del cliente seleccionado en la tabla de clientes en los campos de la ventana de facturas
        :return:  None
        """
        try:
            Facturas.limpiar_factura(self)
            fila = var.ui.tabClientes.selectedItems()
            datos = [var.ui.txtDniFac, var.ui.txtMatriculaFac]
            row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])

            date = QtCore.QDate.currentDate()
            var.ui.txtFechaFac.setText(date.toString('dd/MM/yyyy'))

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al cargar clientee ')
            msg.exec()
            print(error)

    def calcular_subtotal_servicio(self):
        """

        Calcula el subtotal de la linea de venta seleccionada
        :return:  None
        
        """
        try:
            index = 0
            var.ui.tabVentas.setItem(index, 3, QtWidgets.QTableWidgetItem(str('0')))

            if var.txtUnidades.text() == '':
                var.ui.tabVentas.setItem(index, 3, QtWidgets.QTableWidgetItem(str('0')))
            else:
                precio = var.ui.tabVentas.item(index, 1)
                precio = int(precio.text())
                unidades = var.txtUnidades.text()
                unidades = int(unidades)
                subtotal = precio * unidades
                var.ui.tabVentas.setItem(index, 3, QtWidgets.QTableWidgetItem(str(subtotal)))

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al cargar subtotal servicio ')
            msg.exec()
            print(error)