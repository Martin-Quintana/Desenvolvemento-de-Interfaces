import os



nombre = input('Introduce el nombre del archivo: ')

if os.path.exists(nombre+'.txt'):
    print('El archivo ya existe')
else:
    print('......... Creando archivo .............')
    file = open(nombre + '.txt', 'a')
    file.close()
