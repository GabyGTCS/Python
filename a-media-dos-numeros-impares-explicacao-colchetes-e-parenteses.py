'''
Ler e guardar em uma lista 10 números reais, digitados pelo usuário. 
Em seguida percorrer, para calcular e exibir a média dos numeros a partir de 60.

[]= usado para manipular uma Lista
()=Usado para manipular funções (input, len, print, float, int,...)
'''
Lista1=[0]*10
i=0

while i<len(Lista1):
    Lista1[i]=float(input("Valor: "))
    i=i+1
    
i=0
soma=0.0
contador=0
while i<len(Lista1):
    if Lista1[i]%2==1:
        soma=soma+Lista1[i]
        contador=contador+1
    i=i+1
media=soma/conta
print("A Média dos Numeros Impares é: %f" %media)