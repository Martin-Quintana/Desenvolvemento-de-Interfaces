# Form implementation generated from reading ui file 'C:/Users/marti/Documents/GitHub/Desenvolvemento-de-Interfaces/QuintanaRana/dlgSalir.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgSalir(object):
    def setupUi(self, dlgSalir):
        dlgSalir.setObjectName("dlgSalir")
        dlgSalir.resize(270, 220)
        dlgSalir.setMinimumSize(QtCore.QSize(270, 220))
        dlgSalir.setMaximumSize(QtCore.QSize(270, 220))
        dlgSalir.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(dlgSalir)
        self.buttonBox.setGeometry(QtCore.QRect(-120, 160, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(dlgSalir)
        self.label.setGeometry(QtCore.QRect(110, 120, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dlgSalir)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 111, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/marti/Documents/GitHub/Desenvolvemento-de-Interfaces/QuintanaRana\\img/advertencia.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(dlgSalir)
        self.buttonBox.accepted.connect(dlgSalir.accept) # type: ignore
        self.buttonBox.rejected.connect(dlgSalir.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dlgSalir)

    def retranslateUi(self, dlgSalir):
        _translate = QtCore.QCoreApplication.translate
        dlgSalir.setWindowTitle(_translate("dlgSalir", "Dialog"))
        self.label.setText(_translate("dlgSalir", "Desea Salir"))
