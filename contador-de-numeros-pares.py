'''
Faça um programa que leia 5 valores inteiros.
Conte quantos destes valores digitados são pares 
e mostre esta informação.

n= Numero Total de Repetições
c= Contador de Voltas
x= Imput de usuário
np= Numeros Pares
'''
n=5
c=1
np=0
while c<=n:
    x=int(input("Digite algum Valor: "))
    if x%2==0:
        np=np+1
    c=c+1
print ("%d Numero(s) Par(es) foram digitados." %np)
    
    
