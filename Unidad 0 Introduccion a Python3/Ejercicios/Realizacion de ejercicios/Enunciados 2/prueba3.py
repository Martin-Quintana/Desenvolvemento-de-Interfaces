op = 1
while ( op != 0 ):
    print('1- Entrada en Kelvin')
    print('2- Entrada en Farhenheit')
    print('3- Entrada en Celsius')
    print('Pulse 0 para salir')
    op = int(input('Elija opcion: '))

    if (op == 1 ):
        temp = float(input('Introduce la temperatura en Kelvin'))
        celsius = temp - 273.1
        farhenheit = 1.4*temp +32

        print('RESULTADOS')
        print('Temperatura en celsius es: ', round(celsius,2))
        print('Temperatura en farhenheit es: ', round(farhenheit,2))

    elif (op == 2):
        temp = float(input('Introduce la temperatura en Farhenheit'))
        celsius = (temp-32)/1.4
        kelvin = 273.1 + celsius

        print('RESULTADOS')
        print('Temperatura en celsius es: ', round(celsius,2))
        print('Temperatura en kelvin es: ', round(kelvin,2))

    elif (op == 3):
        temp = float(input('Introduce la temperatura en Celsius'))
        kelvin = temp + 273.1
        farhenheit = 1.4 * temp + 32

        print('RESULTADOS')
        print('Temperatura en kelvin es: ', round(kelvin,2))
        print('Temperatura en farhenheit es: ', round(farhenheit,2))

