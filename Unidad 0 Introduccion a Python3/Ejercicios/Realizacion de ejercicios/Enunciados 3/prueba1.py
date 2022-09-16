import random
op = 1

while ( op != 0 ):
    print('')
    print('================================================')
    print('1- Generador de Apuestas de la Primitiva')
    print('2- Generador de Euromillones')
    print('3- Generador de Quiniela')
    print('4- Generador de Loteria Nacional')
    print('Pulse 0 para salir')
    op = int(input('Elija opcion: '))

    if (op == 1 ):

        for i in range(1, 7 ):
            numRandom = int(random.randint(1, 49))
            print(numRandom , end=' ')
    elif (op == 2 ):

        for i in range(1, 6 ):
            numRandom = int(random.randint(1, 50))
            print(numRandom , end=' ')

        for i in range(1, 6):
            numRandom = int(random.randint(1, 9))
            print('Numeros estrella', numRandom, end=' ')