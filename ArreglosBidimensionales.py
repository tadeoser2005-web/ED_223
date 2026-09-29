matriz = [
    [1,2,3],
    [4,5,6]
]

for f in matriz:
    print(f,"\n")


print("\n Acceder al valor 6")
print(matriz[1][2])


print("\n Mostramos la fila uno")
print(matriz[0])

matriz[0][0] = 0


print("\n Cambiamos el elemento en la posicion 0,0")
print(matriz[0][0])

matriz.append([7,8,9])


print("\nagregamos una fila mas")
for f in matriz:
 print(f)


matriz[0].pop(2)

for f in matriz:
 print(f)