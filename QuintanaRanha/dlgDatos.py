# Form implementation generated from reading ui file 'dlgDatos.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgDatos(object):
    def setupUi(self, dlgDatos):
        dlgDatos.setObjectName("dlgDatos")
        dlgDatos.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        dlgDatos.resize(400, 300)
        dlgDatos.setMinimumSize(QtCore.QSize(400, 300))
        dlgDatos.setMaximumSize(QtCore.QSize(400, 300))
        dlgDatos.setModal(True)
        self.label = QtWidgets.QLabel(dlgDatos)
        self.label.setGeometry(QtCore.QRect(70, 130, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.label.setStyleSheet("color: rgb(81, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName("label")
        self.btnExportaDatos = QtWidgets.QPushButton(dlgDatos)
        self.btnExportaDatos.setGeometry(QtCore.QRect(170, 210, 75, 23))
        self.btnExportaDatos.setObjectName("btnExportaDatos")
        self.label_2 = QtWidgets.QLabel(dlgDatos)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 101, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/interrogante.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(dlgDatos)
        self.widget.setGeometry(QtCore.QRect(140, 170, 127, 19))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chkClientes = QtWidgets.QCheckBox(self.widget)
        self.chkClientes.setObjectName("chkClientes")
        self.horizontalLayout.addWidget(self.chkClientes)
        self.chkCoches = QtWidgets.QCheckBox(self.widget)
        self.chkCoches.setObjectName("chkCoches")
        self.horizontalLayout.addWidget(self.chkCoches)

        self.retranslateUi(dlgDatos)
        QtCore.QMetaObject.connectSlotsByName(dlgDatos)

    def retranslateUi(self, dlgDatos):
        _translate = QtCore.QCoreApplication.translate
        dlgDatos.setWindowTitle(_translate("dlgDatos", "Exportar Datos"))
        self.label.setText(_translate("dlgDatos", "Elija los datos que desea exportar:"))
        self.btnExportaDatos.setText(_translate("dlgDatos", "Aceptar"))
        self.chkClientes.setText(_translate("dlgDatos", "Clientes"))
        self.chkCoches.setText(_translate("dlgDatos", "Coches"))
