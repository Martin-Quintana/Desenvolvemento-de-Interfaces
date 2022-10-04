import sys

import var

'''
Eventos generales
'''
class Eventos:
    def Salir(self):
        try:
            var.avisosalir.show()
            #sys.exit()
        except Exception as error:
            print("Error en función salir %s", str(error))

