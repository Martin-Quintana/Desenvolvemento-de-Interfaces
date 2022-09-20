import random

cant = int(input('Introduce la cantidad de elementos que quieres que tenga la lista: '))

lista = []

for i in range(cant):
    lista.append(random.randint(0,10))
    print(lista[i], end=' ')

op = 1

while op != 0:
    print(' ')
    print('================================================')
    print('1- Ordenar la lista y que la muestre por pantalla')
    print('2- Borre un elemento solicitado por teclado')
    print('3- Anhada un elemento aleatorio al final')
    print('4- Tomar los elemntos que estean entre N/5 y N/3 posiciones (Division entera)')
    print('Pulse 0 para salir')
    op = int(input('Elija opcion: '))

    # Ordenar la lista y que la muestre por pantalla
    if op == 1:
        lista.sort()
        print(lista)

    # Borre un elemento solicitado por teclado
    if op == 2:
        solicitado = int(input('Dime que elemento quieres borrar: '))
        lista.remove(solicitado)
        print(lista)

    # Anhada un elemento aleatorio al final
    if op == 3:
         lista.append(random.randint(0,10))
         print(lista)

    # 4- Tomar los elemntos que estean entre N/5 y N/3 posiciones (Division entera)
    if op == 4:
        dividendo = lista[4]
        divisor = lista[2]
        division = dividendo/divisor
        print(division)

