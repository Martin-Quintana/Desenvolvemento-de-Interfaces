import random

numRandom = int(random.randint(1, 100))
print(numRandom)

jugador1 = str(input('Introduce mombre de jugador 1: '))

jugador2 = str(input('Introduce mombre de jugador 2: '))
print(jugador1)
numUser = int(input('Dime un numero del 1 al 100 para intentar adivinarlo: '))

while (numUser != numRandom):
    if (numUser < numRandom):
        print('El numero es mas pequeno')
    else:
        print('El numero es mas grande')
    print(jugador2)
    numUser2 = int(input('Dime un numero del 1 al 100 para intentar adivinarlo: '))
print('ENHORABUENA')
