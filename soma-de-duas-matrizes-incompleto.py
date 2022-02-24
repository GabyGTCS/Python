'''

ler matrizes para duas matrizes 2x3. Crie mais uma matriz com o resultado da soma dos 
elementos das anteriores
'''
grelhaA=[0]*2
for linha in range(len(grelhaA)):
    grelhaA[linha]=[0]*3
    for coluna in range (len(grelhaA[linha])):
        grelhaA[linha][coluna] = int(input("Digite um Valor: "))
print(grelhaA)

grelhaB=[0]*2
for linha in range(len(grelhaB)):
    grelhaB[linha]=[0]*3
    for coluna in range (len(grelhaB[linha])):
        grelhaB[linha][coluna] = int(input("Digite um Valor: "))
print(grelhaB)

grelhaC=[0]*2
print("Matriz C")
for linha in range (len(grelhaC)):
    grelhaC[linha]=[0]*3
    for coluna in range(len(grelhaC[linha])):
        grelhaC [linha] [coluna] = grelhaA [linha] [coluna] + grelhaB [linha] [coluna]
print(grelhaA)
print(grelhaB)
print(grelhaC)
