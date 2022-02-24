'''
Ler e guardar em uma lista 10 números reais, digitados pelo usuário. 
Em seguida percorrer, para calcular e exibir a média dos numeros a partir de 60.

'''
num=[0.0]*10
i=0

while i<len(num):
    num[i]=float(input("Digite um valor: "))
    i=i+1
    
i=0
soma=0.0
contador=0
while i<len(num):
    if num[i]>=60:
        soma=soma+num[i]
        contador=contador+1
    i=i+1
 
print("A média dos valores a partir de 60: %.1f" %media)
