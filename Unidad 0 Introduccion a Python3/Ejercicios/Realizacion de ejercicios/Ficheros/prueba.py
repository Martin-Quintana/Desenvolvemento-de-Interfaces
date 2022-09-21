nombre = input('Introduce el nombre del archivo: ')
print('......... Creando archivo .............')
file = open(nombre + '.txt', 'a')
file.close()
