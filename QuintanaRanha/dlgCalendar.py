# Form implementation generated from reading ui file 'C:/Users/a21martinqr/Documents/GitHub/Desenvolvemento-de-Interfaces/QuintanaRanha/dlgCalendar.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgCalendar(object):
    def setupUi(self, dlgCalendar):
        dlgCalendar.setObjectName("dlgCalendar")
        dlgCalendar.resize(320, 190)
        self.Calendar = QtWidgets.QCalendarWidget(dlgCalendar)
        self.Calendar.setGeometry(QtCore.QRect(0, 0, 320, 190))
        self.Calendar.setMinimumSize(QtCore.QSize(320, 190))
        self.Calendar.setMaximumSize(QtCore.QSize(240, 170))
        self.Calendar.setObjectName("Calendar")

        self.retranslateUi(dlgCalendar)
        QtCore.QMetaObject.connectSlotsByName(dlgCalendar)

    def retranslateUi(self, dlgCalendar):
        _translate = QtCore.QCoreApplication.translate
        dlgCalendar.setWindowTitle(_translate("dlgCalendar", "Fecha Alta"))
