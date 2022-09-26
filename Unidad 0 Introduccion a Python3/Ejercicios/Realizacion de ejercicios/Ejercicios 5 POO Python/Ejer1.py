
class Cuenta :
    
    #Constructor
    def __init__(self, titular, cantidad = 0) :
        self.titular = titular
        self.cantidad = cantidad
        return
        
    #Getters&Setters    
    def get_titular(self) :
        return self.titular
        
    def get_cantidad(self) :
        return self.cantidad
        
    def set_titular(self, t) :
        self.titular = t
        
    def set_cantidad(self, c) :
        self.cantidad = c
    
    #Métodos
    def mostrar(self) :
        print()
        print('     ·Datos de la cuenta:\n\t\t- Titular:', self.titular, '\n\t\t- Cantidad', self.cantidad)
        return
        
    def ingresar(self, c) :
        self.cantidad += c
        print()
        print('     ·Se han ingresado', c, 'euros en la cuenta.')
        print('       >> TOTAL :', self.cantidad, 'euros.')
        
    def retirar(self, c) :
        self.cantidad -= c
        print()
        print('     ·Se han retirado', c, 'euros de la cuenta.')
        print('       >> RESTANTE :', self.cantidad, 'euros.')

cta = Cuenta('0123456789', 100)

print()
cta.mostrar()
print()
cta.ingresar(200)
print()
cta.retirar(400)