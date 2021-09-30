matriz = [[[], [], []], [[], [], []], [[], [], []]]
cont = 0
for l in range(0, 3):
    for c in range(0, 3):
        cont += 1
        matriz[l][c] = cont
print(matriz)

