segundos = input('Indica el numero en segundos')
horas = int(segundos)/3600
resto = int(segundos)%3600
min = int(resto)/60
segf = int(resto)%60
print(segf)
print('Los ', segundos, ' segundos son ', int(horas), 'horas', int(min), 'minutos y ', segf ,' segundos' )
print('=================================================================')
ho = input('Indique numero de horas: ')
minu = input('Indique numero de minutos: ')
se = input('Indique numero de segundos: ')
total = int(ho)*3600 + int(minu)*60 + int(se)
print('El numero total de tiempo en segundos es: ', total)