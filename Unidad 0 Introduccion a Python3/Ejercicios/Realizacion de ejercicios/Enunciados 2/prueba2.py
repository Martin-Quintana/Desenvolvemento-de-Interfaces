import random

numRandom = int(random.randint(1, 100))
print(numRandom)

contador1 = 1
contador2 = 1
jugador1 = str(input('Introduce mombre de jugador 1: '))
jugador2 = str(input('Introduce mombre de jugador 2: '))
print(jugador1)
numUser = int(input('Dime un numero del 1 al 100 para intentar adivinarlo: '))

while (numUser != numRandom):
    if (numUser > numRandom):
        print('El numero es mas pequeno')
    else:
        print('El numero es mas grande')
    contador1 = contador1 +1
    numUser = int(input('Dime un numero del 1 al 100 para intentar adivinarlo: '))
print('ENHORABUENA')


numRandom = int(random.randint(1, 100))
print(numRandom)
print(jugador2)
numUser = int(input('Dime un numero del 1 al 100 para intentar adivinarlo: '))
while (numUser != numRandom):
    if (numUser > numRandom):
        print('El numero es mas pequeno')
    else:
        print('El numero es mas grande')
        contador2 = contador2 + 1
    print(jugador2)
    numUser = int(input('Dime un numero del 1 al 100 para intentar adivinarlo: '))
print('ENHORABUENA')

print('Vamos a ver quien ha ganado')
print(jugador1, 'tiene ', contador1, ' intentos')
print(jugador2, 'tiene ', contador2, ' intentos')

if (contador1 < contador2):
    print('Gano ', jugador1)
elif(contador1 == contador2):
    print('Habeis empatado')
else:
    print('Gano ', jugador2)