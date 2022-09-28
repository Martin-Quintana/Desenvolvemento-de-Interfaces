import sys
'''
Eventos generales
'''
class Eventos:
    def Salir(self):
        try:
            sys.exit()
        except Exception as error:
            print("Error en función salir %s", str(error))

