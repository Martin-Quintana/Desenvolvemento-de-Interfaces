nombre = [('Pepito', 1500), ('Manolito', 5000), ('Joselito', 4566), ('Lola', 5464), ('Tiburon',985545)]



for i in range (len(nombre)):
    print(nombre[i][0])
    for j in range(len(nombre)):
        print(nombre[0][j])




nombre.sort(key= lambda x: x[1], reverse=True)

