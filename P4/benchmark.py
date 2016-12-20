import random
import time

filas = 3000
columnas = 3000

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
inicio = time.clock()
for i in range(filas):
    matrizSol.append([])
    for j in range(columnas):
        matrizSol[i].append((matrizA[i][j]*matrizB[i][j]))

final = time.clock()

total = final - inicio

print("El tiempo que ha tardado es",total*10," s")