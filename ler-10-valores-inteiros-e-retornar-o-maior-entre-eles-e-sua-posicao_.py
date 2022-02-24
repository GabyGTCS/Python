'''

Leia 10 valores inteiros. Apresente então o maior valor lido e a
posição dentre os 10 valores lidos.

'''
n=10
c=1
p=1
while c<=n:
    x=int(input("Digite Um Numero: "))
    if c==1:
        m=x
    elif x>m:
        m=x
        p=c
    c=c+1
print("O maior Valor lido é %d , e é o %d o. Numero digitado." % (m,p))