'''
URI Online Judge | 1064

Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. 
Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.
'''
lista=[]
lista2=[]
for i in range (6):
    lista.append(float(input()))
    if lista[i]>0:
        lista2.append(lista[i])
m=sum(lista2)/len(lista2)
print ("%d valores positivos" %len(lista2))
print("%.1f" %m)

