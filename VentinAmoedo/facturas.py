from PyQt6 import QtWidgets, QtCore
import conexion
import var


class Facturas():
    def cargaLineaVenta(index):
        try:
            index = 0
            var.cmbServicio = QtWidgets.QComboBox()
            var.cmbServicio.setFixedSize(160, 20)
            var.txtUnidades = QtWidgets.QLineEdit()
            var.txtUnidades.setFixedSize(150, 20)
            var.ui.tabVentas.setRowCount(index + 1)
            var.ui.tabVentas.setCellWidget(index, 1, var.cmbServicio)
            var.ui.tabVentas.setCellWidget(index, 3, var.txtUnidades)

        except Exception as error:
            print('error carga linea ventas', error)