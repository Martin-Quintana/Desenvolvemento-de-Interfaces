import random

LIMITE = 7.5
baraja = [1, 2, 3, 4, 5, 6, 7, 0.5, 0.5, 0.5] * 4
mano = []
play = True


while play:
    # Pide y guarda el numero
    posicion_aleatoria = random.randint(0, len(baraja) - 1)
    carta_aletatorio = baraja.pop(posicion_aleatoria)
    mano.append(carta_aletatorio)
    print('Mi mano: {mano}'.format(mano=mano))

    # Sumamos mi mano
    suma_total = 0
    for carta in mano:
        suma_total += carta

    print('Tengo {total} puntos'.format(total=suma_total))

    # Preguntar si nos queremos plantar
    respuesta = input('¿Te plantas?: ')
    respuesta.lower()
    if respuesta == 'si':
        play = False
    else:
        # Comprobamos si ha ganado o perdido
        if suma_total > LIMITE:
            print('Has perdido con {total}'.format(total=suma_total))
            play = False
        elif suma_total == LIMITE:
            print('Has ganado!!!')
            play = False

