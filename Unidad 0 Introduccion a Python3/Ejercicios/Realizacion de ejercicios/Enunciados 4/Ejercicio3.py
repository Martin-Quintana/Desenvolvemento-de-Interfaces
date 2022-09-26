nombre = [('Pepito', 1500),
          ('Manolito', 5000),
          ('Joselito', 4566),
          ('Lola', 5464),
          ('Tiburon',985545)]
print(nombre)

for i in range (len(nombre)):
    print(nombre[i][0])

nombre.sort(key= lambda x: x[1], reverse=True)

print(nombre)