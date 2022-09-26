
class Cuenta:

    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def cantidad(self):
        return self.__cantidad

    def retirar(self, importe):
        if (importe > 0):
            self.__cantidad = self.__cantidad - importe
            print("Importe retirado: " + str(importe) + "€")
        else:
            self.__cantidad = self.__cantidad
            print("No es posible retirar " + str(importe) + "€")

    def ingresar(self, importe):
        if (importe < 0):
            self.__cantidad = self.__cantidad
            print("No es posible ingresar " + str(importe) + "€")
        else:
            self.__cantidad = self.__cantidad + importe
            print("Importe ingresado: " + str(importe) + "€")

    def mostrar(self):
        return self.__titular.mostrar() + " " + str(self.__cantidad) + "€"