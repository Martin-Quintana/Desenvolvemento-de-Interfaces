import random
cant = int(input('Introduce la cantidad de elementos que quieres que tenga la lista: '))

lista = {}

for i in range(cant):
    lista[i] = int(random.randint(1, 10))
    print(lista[i], end=' ')