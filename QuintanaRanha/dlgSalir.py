# Form implementation generated from reading ui file 'dlgSalir.ui'
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

        self.retranslateUi(dlgSalir)
        self.buttonBox.accepted.connect(dlgSalir.accept) # type: ignore
        self.buttonBox.rejected.connect(dlgSalir.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dlgSalir)

    def retranslateUi(self, dlgSalir):
        _translate = QtCore.QCoreApplication.translate
        dlgSalir.setWindowTitle(_translate("dlgSalir", "Dialog"))
