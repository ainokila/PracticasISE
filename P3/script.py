import random

filas = 1000
columnas = 1000

matrizA= []
for i in range(filas):
    matrizA.append([])
    for j in range(columnas):
        matrizA[i].append(random.randint(0,100))

matrizB= []
for i in range(filas):
    matrizB.append([])
    for j in range(columnas):
        matrizB[i].append(random.randint(0,100))



matrizSol=[]
for i in range(filas):
    matrizSol.append([])
    for j in range(columnas):
        matrizSol[i].append((matrizA[i][j]*matrizB[i][j]))


print(matrizSol)