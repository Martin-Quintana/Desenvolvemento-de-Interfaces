import matplotlib.pyplot as plt
from pylab import *
import random, os
import tqdm
os.system('csl')
resultado = {'Dos': 0,  'Tres': 0, 'Cuatro': 0,
             'Cinco': 0, 'Seis': 0, 'Siete': 0,
             'Ocho': 0, 'Nueve': 0, 'Diez': 0,
             'Once': 0, 'Doce': 0,}

grafica = []

var = int(input('Indica numer de tiradas: '))
print('\n')

for i in tqdm(range(var)):
    dado1 = random(randint(1,6))
    dado2 = random(randint(1,6))
    dado = dado1+dado2

    if dado == 2:
        resultado['Dos'] += 1
    elif dado == 3:
        resultado['Tres'] += 1
    elif dado == 4:
        resultado['Cuatro'] += 1
    elif dado == 5:
        resultado['Cinco'] += 1
    elif dado == 6:
        resultado['Seis'] += 1
    elif dado == 7:
        resultado['Siete'] += 1
    elif dado == 8:
        resultado['Ocho'] += 1
    elif dado == 9:
        resultado['Nueve'] += 1