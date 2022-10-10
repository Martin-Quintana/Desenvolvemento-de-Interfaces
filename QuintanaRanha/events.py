import sys

import sys,var

'''
Eventos generales
'''
class Eventos:
    def Salir(self):
        try:
            var.avisosalir.show()
            if var.avisosalir.exec():
                sys.exit()
            else:
                var.avisosalir.hide()
            #sys.exit()
        except Exception as error:
            print("Error en función salir %s", str(error))

    def abrirCalendar (self = None):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error abrir calendario', error)

