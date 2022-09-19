import random

op = 1

while op != 0:
    print(' ')
    print('================================================')
    print('1- Generador de Apuestas de la Primitiva')
    print('2- Generador de Euromillones')
    print('3- Generador de Quiniela')
    print('4- Generador de Loteria Nacional')
    print('Pulse 0 para salir')
    op = int(input('Elija opcion: '))

    # Generador de Apuestas de la Primitiva
    if op == 1:

        for i in range(1, 7):
            numRandom = int(random.randint(1, 49))
            print(numRandom, end=' ')

    # Generador de Euromillones
    elif op == 2:

        for i in range(1, 6):
            numRandom = int(random.randint(1, 50))
            print(numRandom, end=' ')

        for i in range(1, 2):
            numRandom = int(random.randint(1, 9))
            numRandom2 = int(random.randint(1, 9))
            print('Numeros estrella', numRandom, ' ', numRandom2, end=' ')

    # Generador de Quiniela
    elif op == 3:

        opcion = ['1', 'X', '2']
        for i in range(1, 16):
            numRandom = int(random.randint(1, 3))
            print(opcion, end=' ')

    # Generador de Loteria Nacional
    elif op == 4:
        numRandom = int(random.randint(0, 99999))
        print('El numero de la loteria nacional es: ', numRandom, end=' ')
