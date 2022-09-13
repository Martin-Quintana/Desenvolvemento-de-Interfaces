print('==============================')
print('Calculo coste envio')
print('==============================')
numbon = input('Numero de bonecas del envio: ')
numpall = input('Numero de pallasos del envio: ')
peso = float(numbon)*75 + float(numpall)*112

total = peso/1000

print('Peso total en kilos es: ', total)

precioenvio = float(total)*3.5

print('El precio del envio es: ', precioenvio)