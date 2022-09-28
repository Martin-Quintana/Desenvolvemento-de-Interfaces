# Form implementation generated from reading ui file 'ventMain.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ventMain(object):
    def setupUi(self, ventMain):
        ventMain.setObjectName("ventMain")
        ventMain.resize(800, 600)
        ventMain.setMinimumSize(QtCore.QSize(800, 600))
        ventMain.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(ventMain)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitulocli = QtWidgets.QLabel(self.centralwidget)
        self.lblTitulocli.setGeometry(QtCore.QRect(320, 10, 150, 20))
        self.lblTitulocli.setMinimumSize(QtCore.QSize(150, 20))
        self.lblTitulocli.setMaximumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulocli.setFont(font)
        self.lblTitulocli.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblTitulocli.setObjectName("lblTitulocli")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(80, 40, 574, 28))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblDni = QtWidgets.QLabel(self.widget)
        self.lblDni.setMinimumSize(QtCore.QSize(30, 20))
        self.lblDni.setMaximumSize(QtCore.QSize(30, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblDni.setFont(font)
        self.lblDni.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblDni.setObjectName("lblDni")
        self.horizontalLayout.addWidget(self.lblDni)
        self.txtDni = QtWidgets.QLineEdit(self.widget)
        self.txtDni.setMinimumSize(QtCore.QSize(100, 20))
        self.txtDni.setMaximumSize(QtCore.QSize(100, 20))
        self.txtDni.setObjectName("txtDni")
        self.horizontalLayout.addWidget(self.txtDni)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lblNombre = QtWidgets.QLabel(self.widget)
        self.lblNombre.setMinimumSize(QtCore.QSize(50, 20))
        self.lblNombre.setMaximumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre.setFont(font)
        self.lblNombre.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblNombre.setObjectName("lblNombre")
        self.horizontalLayout.addWidget(self.lblNombre)
        self.txtNombre = QtWidgets.QLineEdit(self.widget)
        self.txtNombre.setMinimumSize(QtCore.QSize(200, 20))
        self.txtNombre.setMaximumSize(QtCore.QSize(200, 20))
        self.txtNombre.setObjectName("txtNombre")
        self.horizontalLayout.addWidget(self.txtNombre)
        self.lblFechaltacli = QtWidgets.QLabel(self.widget)
        self.lblFechaltacli.setMinimumSize(QtCore.QSize(68, 20))
        self.lblFechaltacli.setMaximumSize(QtCore.QSize(68, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblFechaltacli.setFont(font)
        self.lblFechaltacli.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblFechaltacli.setObjectName("lblFechaltacli")
        self.horizontalLayout.addWidget(self.lblFechaltacli)
        self.txtFechaltacli = QtWidgets.QLineEdit(self.widget)
        self.txtFechaltacli.setMinimumSize(QtCore.QSize(60, 20))
        self.txtFechaltacli.setMaximumSize(QtCore.QSize(60, 20))
        self.txtFechaltacli.setObjectName("txtFechaltacli")
        self.horizontalLayout.addWidget(self.txtFechaltacli)
        self.btnFechaltacli = QtWidgets.QPushButton(self.widget)
        self.btnFechaltacli.setMinimumSize(QtCore.QSize(22, 22))
        self.btnFechaltacli.setMaximumSize(QtCore.QSize(22, 22))
        self.btnFechaltacli.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/calendar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnFechaltacli.setIcon(icon)
        self.btnFechaltacli.setIconSize(QtCore.QSize(19, 19))
        self.btnFechaltacli.setObjectName("btnFechaltacli")
        self.horizontalLayout.addWidget(self.btnFechaltacli)
        ventMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ventMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        ventMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ventMain)
        self.statusbar.setObjectName("statusbar")
        ventMain.setStatusBar(self.statusbar)
        self.actionSalir = QtGui.QAction(ventMain)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(ventMain)
        QtCore.QMetaObject.connectSlotsByName(ventMain)

    def retranslateUi(self, ventMain):
        _translate = QtCore.QCoreApplication.translate
        ventMain.setWindowTitle(_translate("ventMain", "Talleres Teis"))
        self.lblTitulocli.setText(_translate("ventMain", "XESTIÓN CLIENTES"))
        self.lblDni.setText(_translate("ventMain", "DNI:"))
        self.lblNombre.setText(_translate("ventMain", "Nombre:"))
        self.lblFechaltacli.setText(_translate("ventMain", "Fecha Alta:"))
        self.menuArchivo.setTitle(_translate("ventMain", "Archivo"))
        self.actionSalir.setText(_translate("ventMain", "Salir"))
        self.actionSalir.setShortcut(_translate("ventMain", "Alt+S"))
