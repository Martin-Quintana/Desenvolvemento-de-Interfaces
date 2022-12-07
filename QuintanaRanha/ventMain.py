# Form implementation generated from reading ui file 'ventMain.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ventMain(object):
    def setupUi(self, ventMain):
        ventMain.setObjectName("ventMain")
        ventMain.resize(800, 620)
        ventMain.setMinimumSize(QtCore.QSize(800, 620))
        ventMain.setMaximumSize(QtCore.QSize(800, 620))
        self.centralwidget = QtWidgets.QWidget(ventMain)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 620))
        self.tabWidget.setMinimumSize(QtCore.QSize(800, 620))
        self.tabWidget.setMaximumSize(QtCore.QSize(800, 620))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btnBuscacli = QtWidgets.QPushButton(self.tab)
        self.btnBuscacli.setGeometry(QtCore.QRect(690, 150, 28, 28))
        self.btnBuscacli.setMinimumSize(QtCore.QSize(28, 28))
        self.btnBuscacli.setMaximumSize(QtCore.QSize(28, 28))
        self.btnBuscacli.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/lupa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnBuscacli.setIcon(icon)
        self.btnBuscacli.setIconSize(QtCore.QSize(20, 20))
        self.btnBuscacli.setObjectName("btnBuscacli")
        self.lblTituloCli = QtWidgets.QLabel(self.tab)
        self.lblTituloCli.setGeometry(QtCore.QRect(330, 0, 150, 20))
        self.lblTituloCli.setMinimumSize(QtCore.QSize(150, 20))
        self.lblTituloCli.setMaximumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblTituloCli.setFont(font)
        self.lblTituloCli.setAutoFillBackground(False)
        self.lblTituloCli.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 255, 255), stop:1 rgba(255, 255, 255, 255))")
        self.lblTituloCli.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblTituloCli.setObjectName("lblTituloCli")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 30, 614, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblDni = QtWidgets.QLabel(self.layoutWidget)
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
        self.txtDni = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtDni.setMinimumSize(QtCore.QSize(100, 20))
        self.txtDni.setMaximumSize(QtCore.QSize(100, 20))
        self.txtDni.setStyleSheet("background-color:rgb(255, 255, 127)")
        self.txtDni.setObjectName("txtDni")
        self.horizontalLayout.addWidget(self.txtDni)
        self.lblValidarDni = QtWidgets.QLabel(self.layoutWidget)
        self.lblValidarDni.setMinimumSize(QtCore.QSize(20, 20))
        self.lblValidarDni.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblValidarDni.setFont(font)
        self.lblValidarDni.setText("")
        self.lblValidarDni.setObjectName("lblValidarDni")
        self.horizontalLayout.addWidget(self.lblValidarDni)
        self.lblNombre = QtWidgets.QLabel(self.layoutWidget)
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
        self.txtNombre = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtNombre.setMinimumSize(QtCore.QSize(200, 20))
        self.txtNombre.setMaximumSize(QtCore.QSize(200, 20))
        self.txtNombre.setObjectName("txtNombre")
        self.horizontalLayout.addWidget(self.txtNombre)
        self.lblFechaltacli = QtWidgets.QLabel(self.layoutWidget)
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
        self.txtFechaltacli = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtFechaltacli.setMinimumSize(QtCore.QSize(80, 20))
        self.txtFechaltacli.setMaximumSize(QtCore.QSize(80, 20))
        self.txtFechaltacli.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtFechaltacli.setObjectName("txtFechaltacli")
        self.horizontalLayout.addWidget(self.txtFechaltacli)
        self.btnFechaltacli = QtWidgets.QPushButton(self.layoutWidget)
        self.btnFechaltacli.setMinimumSize(QtCore.QSize(22, 22))
        self.btnFechaltacli.setMaximumSize(QtCore.QSize(22, 22))
        self.btnFechaltacli.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/calendar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnFechaltacli.setIcon(icon1)
        self.btnFechaltacli.setIconSize(QtCore.QSize(19, 19))
        self.btnFechaltacli.setObjectName("btnFechaltacli")
        self.horizontalLayout.addWidget(self.btnFechaltacli)
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(220, 190, 340, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rbtGasolina = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.rbtGasolina.setMinimumSize(QtCore.QSize(80, 20))
        self.rbtGasolina.setMaximumSize(QtCore.QSize(80, 20))
        self.rbtGasolina.setChecked(True)
        self.rbtGasolina.setObjectName("rbtGasolina")
        self.horizontalLayout_4.addWidget(self.rbtGasolina)
        self.rbtDiesel = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.rbtDiesel.setMinimumSize(QtCore.QSize(80, 20))
        self.rbtDiesel.setMaximumSize(QtCore.QSize(80, 20))
        self.rbtDiesel.setObjectName("rbtDiesel")
        self.horizontalLayout_4.addWidget(self.rbtDiesel)
        self.rbtHibrido = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.rbtHibrido.setMinimumSize(QtCore.QSize(80, 20))
        self.rbtHibrido.setMaximumSize(QtCore.QSize(80, 20))
        self.rbtHibrido.setObjectName("rbtHibrido")
        self.horizontalLayout_4.addWidget(self.rbtHibrido)
        self.rbtElectrico = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.rbtElectrico.setMinimumSize(QtCore.QSize(80, 20))
        self.rbtElectrico.setMaximumSize(QtCore.QSize(80, 20))
        self.rbtElectrico.setObjectName("rbtElectrico")
        self.horizontalLayout_4.addWidget(self.rbtElectrico)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(10, 240, 780, 16))
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.btnLimpiacli = QtWidgets.QPushButton(self.tab)
        self.btnLimpiacli.setGeometry(QtCore.QRect(690, 190, 28, 28))
        self.btnLimpiacli.setMinimumSize(QtCore.QSize(28, 28))
        self.btnLimpiacli.setMaximumSize(QtCore.QSize(28, 28))
        self.btnLimpiacli.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/limpiar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnLimpiacli.setIcon(icon2)
        self.btnLimpiacli.setIconSize(QtCore.QSize(20, 20))
        self.btnLimpiacli.setObjectName("btnLimpiacli")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_3.setGeometry(QtCore.QRect(270, 220, 239, 22))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnGuardacli = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btnGuardacli.setMinimumSize(QtCore.QSize(75, 20))
        self.btnGuardacli.setMaximumSize(QtCore.QSize(275, 20))
        self.btnGuardacli.setStyleSheet("background-color: rgb(0, 255, 255)")
        self.btnGuardacli.setObjectName("btnGuardacli")
        self.horizontalLayout_5.addWidget(self.btnGuardacli)
        self.btnModifcli = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btnModifcli.setMinimumSize(QtCore.QSize(75, 20))
        self.btnModifcli.setMaximumSize(QtCore.QSize(75, 20))
        self.btnModifcli.setStyleSheet("background-color: rgb(0, 255, 255)")
        self.btnModifcli.setObjectName("btnModifcli")
        self.horizontalLayout_5.addWidget(self.btnModifcli)
        self.btnBorracli = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btnBorracli.setMinimumSize(QtCore.QSize(75, 20))
        self.btnBorracli.setMaximumSize(QtCore.QSize(75, 20))
        self.btnBorracli.setStyleSheet("background-color: rgb(0, 255, 255)")
        self.btnBorracli.setObjectName("btnBorracli")
        self.horizontalLayout_5.addWidget(self.btnBorracli)
        self.tabClientes = QtWidgets.QTableWidget(self.tab)
        self.tabClientes.setGeometry(QtCore.QRect(10, 260, 780, 250))
        self.tabClientes.setMinimumSize(QtCore.QSize(780, 250))
        self.tabClientes.setMaximumSize(QtCore.QSize(780, 250))
        self.tabClientes.setAlternatingRowColors(True)
        self.tabClientes.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tabClientes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabClientes.setObjectName("tabClientes")
        self.tabClientes.setColumnCount(6)
        self.tabClientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(5, item)
        self.layoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_4.setGeometry(QtCore.QRect(50, 60, 698, 22))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblDirCli = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDirCli.setFont(font)
        self.lblDirCli.setObjectName("lblDirCli")
        self.horizontalLayout_2.addWidget(self.lblDirCli)
        self.txtDirCli = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.txtDirCli.setMinimumSize(QtCore.QSize(200, 20))
        self.txtDirCli.setMaximumSize(QtCore.QSize(200, 20))
        self.txtDirCli.setObjectName("txtDirCli")
        self.horizontalLayout_2.addWidget(self.txtDirCli)
        self.lblProvCli = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblProvCli.setFont(font)
        self.lblProvCli.setObjectName("lblProvCli")
        self.horizontalLayout_2.addWidget(self.lblProvCli)
        self.cmbProcli = QtWidgets.QComboBox(self.layoutWidget_4)
        self.cmbProcli.setMinimumSize(QtCore.QSize(120, 20))
        self.cmbProcli.setMaximumSize(QtCore.QSize(120, 20))
        self.cmbProcli.setObjectName("cmbProcli")
        self.horizontalLayout_2.addWidget(self.cmbProcli)
        self.lblMuniCli = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblMuniCli.setFont(font)
        self.lblMuniCli.setObjectName("lblMuniCli")
        self.horizontalLayout_2.addWidget(self.lblMuniCli)
        self.cmbMunicli = QtWidgets.QComboBox(self.layoutWidget_4)
        self.cmbMunicli.setMinimumSize(QtCore.QSize(180, 20))
        self.cmbMunicli.setMaximumSize(QtCore.QSize(180, 20))
        self.cmbMunicli.setObjectName("cmbMunicli")
        self.horizontalLayout_2.addWidget(self.cmbMunicli)
        self.layoutWidget_5 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_5.setGeometry(QtCore.QRect(150, 160, 470, 22))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblMatricCli = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblMatricCli.setFont(font)
        self.lblMatricCli.setObjectName("lblMatricCli")
        self.horizontalLayout_3.addWidget(self.lblMatricCli)
        self.txtMatricula = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.txtMatricula.setMinimumSize(QtCore.QSize(100, 20))
        self.txtMatricula.setMaximumSize(QtCore.QSize(100, 20))
        self.txtMatricula.setStyleSheet("background-color:rgb(255, 255, 127)")
        self.txtMatricula.setObjectName("txtMatricula")
        self.horizontalLayout_3.addWidget(self.txtMatricula)
        self.lblMarca = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblMarca.setFont(font)
        self.lblMarca.setObjectName("lblMarca")
        self.horizontalLayout_3.addWidget(self.lblMarca)
        self.txtMarca = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.txtMarca.setMinimumSize(QtCore.QSize(100, 20))
        self.txtMarca.setMaximumSize(QtCore.QSize(100, 20))
        self.txtMarca.setObjectName("txtMarca")
        self.horizontalLayout_3.addWidget(self.txtMarca)
        self.lblModelo = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblModelo.setFont(font)
        self.lblModelo.setObjectName("lblModelo")
        self.horizontalLayout_3.addWidget(self.lblModelo)
        self.txtModelo = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.txtModelo.setMinimumSize(QtCore.QSize(100, 20))
        self.txtModelo.setMaximumSize(QtCore.QSize(100, 20))
        self.txtModelo.setObjectName("txtModelo")
        self.horizontalLayout_3.addWidget(self.txtModelo)
        self.lblCarTit = QtWidgets.QLabel(self.tab)
        self.lblCarTit.setGeometry(QtCore.QRect(330, 130, 150, 20))
        self.lblCarTit.setMinimumSize(QtCore.QSize(150, 20))
        self.lblCarTit.setMaximumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblCarTit.setFont(font)
        self.lblCarTit.setAutoFillBackground(False)
        self.lblCarTit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 255, 255), stop:1 rgba(255, 255, 255, 255))")
        self.lblCarTit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblCarTit.setObjectName("lblCarTit")
        self.layoutWidget_6 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_6.setGeometry(QtCore.QRect(220, 90, 341, 22))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.btnGroupPago = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.btnGroupPago.setContentsMargins(0, 0, 0, 0)
        self.btnGroupPago.setObjectName("btnGroupPago")
        self.lblFormapagoCli = QtWidgets.QLabel(self.layoutWidget_6)
        self.lblFormapagoCli.setMinimumSize(QtCore.QSize(0, 20))
        self.lblFormapagoCli.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblFormapagoCli.setFont(font)
        self.lblFormapagoCli.setObjectName("lblFormapagoCli")
        self.btnGroupPago.addWidget(self.lblFormapagoCli)
        self.chkEfec = QtWidgets.QCheckBox(self.layoutWidget_6)
        self.chkEfec.setMinimumSize(QtCore.QSize(0, 20))
        self.chkEfec.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chkEfec.setFont(font)
        self.chkEfec.setObjectName("chkEfec")
        self.btnGroupPago.addWidget(self.chkEfec)
        self.chkTar = QtWidgets.QCheckBox(self.layoutWidget_6)
        self.chkTar.setMinimumSize(QtCore.QSize(0, 20))
        self.chkTar.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chkTar.setFont(font)
        self.chkTar.setObjectName("chkTar")
        self.btnGroupPago.addWidget(self.chkTar)
        self.chkTrans = QtWidgets.QCheckBox(self.layoutWidget_6)
        self.chkTrans.setMinimumSize(QtCore.QSize(0, 20))
        self.chkTrans.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chkTrans.setFont(font)
        self.chkTrans.setObjectName("chkTrans")
        self.btnGroupPago.addWidget(self.chkTrans)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(10, 110, 780, 16))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.chkHistorico = QtWidgets.QCheckBox(self.tab)
        self.chkHistorico.setGeometry(QtCore.QRect(590, 220, 70, 17))
        self.chkHistorico.setObjectName("chkHistorico")
        self.tabWidget.addTab(self.tab, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.tabWidget.addTab(self.tab2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        ventMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ventMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuHerramientas = QtWidgets.QMenu(self.menubar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        ventMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ventMain)
        self.statusbar.setObjectName("statusbar")
        ventMain.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(ventMain)
        self.toolBar.setObjectName("toolBar")
        ventMain.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionSalir = QtGui.QAction(ventMain)
        self.actionSalir.setObjectName("actionSalir")
        self.actionSalibar = QtGui.QAction(ventMain)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/salida.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSalibar.setIcon(icon3)
        self.actionSalibar.setObjectName("actionSalibar")
        self.actionCrear_copia_seguridad = QtGui.QAction(ventMain)
        self.actionCrear_copia_seguridad.setObjectName("actionCrear_copia_seguridad")
        self.actionRestaurar_copia_seguridad = QtGui.QAction(ventMain)
        self.actionRestaurar_copia_seguridad.setObjectName("actionRestaurar_copia_seguridad")
        self.actionpushDB = QtGui.QAction(ventMain)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/pushDB.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionpushDB.setIcon(icon4)
        self.actionpushDB.setObjectName("actionpushDB")
        self.actionpullDB = QtGui.QAction(ventMain)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/pullDB.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionpullDB.setIcon(icon5)
        self.actionpullDB.setObjectName("actionpullDB")
        self.actionExportar_Datos = QtGui.QAction(ventMain)
        self.actionExportar_Datos.setObjectName("actionExportar_Datos")
        self.actionImportar_Datos = QtGui.QAction(ventMain)
        self.actionImportar_Datos.setObjectName("actionImportar_Datos")
        self.actioncambioprocar = QtGui.QAction(ventMain)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/cambioprocar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actioncambioprocar.setIcon(icon6)
        self.actioncambioprocar.setObjectName("actioncambioprocar")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuHerramientas.addAction(self.actionCrear_copia_seguridad)
        self.menuHerramientas.addAction(self.actionRestaurar_copia_seguridad)
        self.menuHerramientas.addSeparator()
        self.menuHerramientas.addAction(self.actionExportar_Datos)
        self.menuHerramientas.addAction(self.actionImportar_Datos)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.toolBar.addAction(self.actioncambioprocar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionpushDB)
        self.toolBar.addAction(self.actionpullDB)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSalibar)

        self.retranslateUi(ventMain)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ventMain)

    def retranslateUi(self, ventMain):
        _translate = QtCore.QCoreApplication.translate
        ventMain.setWindowTitle(_translate("ventMain", "Talleres Teis"))
        self.lblTituloCli.setText(_translate("ventMain", "XESTIÓN CLIENTES"))
        self.lblDni.setText(_translate("ventMain", "DNI:"))
        self.lblNombre.setText(_translate("ventMain", "Nombre:"))
        self.lblFechaltacli.setText(_translate("ventMain", "Fecha Alta:"))
        self.rbtGasolina.setText(_translate("ventMain", "Gasolina"))
        self.rbtDiesel.setText(_translate("ventMain", "Diesel"))
        self.rbtHibrido.setText(_translate("ventMain", "Hibrido"))
        self.rbtElectrico.setText(_translate("ventMain", "Electrico"))
        self.btnGuardacli.setText(_translate("ventMain", "Guardar"))
        self.btnModifcli.setText(_translate("ventMain", "Modificar"))
        self.btnBorracli.setText(_translate("ventMain", "Eliminar"))
        item = self.tabClientes.horizontalHeaderItem(0)
        item.setText(_translate("ventMain", "DNI"))
        item = self.tabClientes.horizontalHeaderItem(1)
        item.setText(_translate("ventMain", "MATRICULA"))
        item = self.tabClientes.horizontalHeaderItem(2)
        item.setText(_translate("ventMain", "MARCA"))
        item = self.tabClientes.horizontalHeaderItem(3)
        item.setText(_translate("ventMain", "MODELO"))
        item = self.tabClientes.horizontalHeaderItem(4)
        item.setText(_translate("ventMain", "MOTOR"))
        item = self.tabClientes.horizontalHeaderItem(5)
        item.setText(_translate("ventMain", "FECHA BAJA"))
        self.lblDirCli.setText(_translate("ventMain", "Direccion:"))
        self.lblProvCli.setText(_translate("ventMain", "Provincia:"))
        self.lblMuniCli.setText(_translate("ventMain", "Municipio:"))
        self.lblMatricCli.setText(_translate("ventMain", "Matricula:"))
        self.lblMarca.setText(_translate("ventMain", "Marca:"))
        self.lblModelo.setText(_translate("ventMain", "Modelo:"))
        self.lblCarTit.setText(_translate("ventMain", "XESTIÓN VEHICULOS"))
        self.lblFormapagoCli.setText(_translate("ventMain", "Forma de Pago:"))
        self.chkEfec.setText(_translate("ventMain", "Efectivo"))
        self.chkTar.setText(_translate("ventMain", "Tarjeta"))
        self.chkTrans.setText(_translate("ventMain", "Transferencia"))
        self.chkHistorico.setText(_translate("ventMain", "Historico"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ventMain", "Clientes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("ventMain", "Facturacion"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("ventMain", "Servizos"))
        self.menuArchivo.setTitle(_translate("ventMain", "Archivo"))
        self.menuHerramientas.setTitle(_translate("ventMain", "Herramientas"))
        self.toolBar.setWindowTitle(_translate("ventMain", "toolBar"))
        self.actionSalir.setText(_translate("ventMain", "Salir"))
        self.actionSalir.setShortcut(_translate("ventMain", "Alt+S"))
        self.actionSalibar.setText(_translate("ventMain", "Salibar"))
        self.actionCrear_copia_seguridad.setText(_translate("ventMain", "Crear Copia Seguridad"))
        self.actionRestaurar_copia_seguridad.setText(_translate("ventMain", "Restaurar Copia Seguridad"))
        self.actionpushDB.setText(_translate("ventMain", "pushDB"))
        self.actionpullDB.setText(_translate("ventMain", "pullDB"))
        self.actionExportar_Datos.setText(_translate("ventMain", "Exportar Datos"))
        self.actionExportar_Datos.setShortcut(_translate("ventMain", "Alt+E"))
        self.actionImportar_Datos.setText(_translate("ventMain", "Importar Datos"))
        self.actionImportar_Datos.setShortcut(_translate("ventMain", "Alt+I"))
        self.actioncambioprocar.setText(_translate("ventMain", "cambioprocar"))
