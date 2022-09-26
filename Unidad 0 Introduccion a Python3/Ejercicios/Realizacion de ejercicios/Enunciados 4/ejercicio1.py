from collections import Counter
import random

cant = int(input('Introduce la cantidad de elementos que quieres que tenga la lista: '))

lista = []

for i in range(cant):
    lista.append(random.randint(0,10))
    print(lista[i], end=' ')

counter = Counter(lista)
first = counter.most_common(1)
print('\n')
print(first)



