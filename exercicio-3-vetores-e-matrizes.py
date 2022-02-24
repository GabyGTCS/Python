'''
Implemente em Python um algoritmo que leia números reais em duas matrizes 3x2 (3 linhas e 2 Colunas.
Calcule o resultado da subtração da primeira pela segunda matriz.

'''
A=[0]*3 
'''Esse primeiro valor cria o numero de Linhas '''

print("MatrizA") 
for linha in range(len(A)):
    A[linha]=[0]*2
    '''Esse segundo valor cria o numero de Colunas'''
    
    for coluna in range(len(A[linha])):
        A[linha][coluna]=float(input("Digite um valor: "))
B=[0]*3
print("MatrizB")
for linha in range(len(B)):
    B[linha]=[0]*2
    for coluna in range(len(B[linha])):
        B[linha][coluna]=float(input("Digite um valor: "))
C=[0]*3
print ("MatrizC")
for linha in range (len(C)):
    C[linha]=[0]*2
    for coluna in range(len(C[linha])):
        C[linha][coluna] = A[linha][coluna]+B[linha][coluna]

print (C)
