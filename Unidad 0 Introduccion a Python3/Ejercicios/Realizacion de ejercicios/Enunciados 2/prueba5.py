num = int(input('Introduce un numero para hacer su factorial: '))

fact = 1

if num == 0:
    print('1')
elif num < 0:
    print('error')
else:

    for i in range(1, num + 1):
        fact = fact * i

    print("El factorial es : ", end="")
    print(fact)