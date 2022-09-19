import random

cant = int(input('Introduce la cantidad de elementos que quieres que tenga la lista: '))

lista = {}

for i in range(cant):
    lista[i] = int(random.randint(1, 10))
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
        print(list.sort(lista,reverse=False))


