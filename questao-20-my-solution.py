'''

Leia 2 valores inteiros X e Y. A seguir, calcule e mostre 
a soma dos números impares entre eles.

'''
x=int(input("insira valor X: "))
y=int(input("insira valor Y: "))
s=0
if x<y:
    #se x é par
    if (x % 2) != 1:
        x=x+1
        while x<=y:
            s=s+x
            print(s)
            x=x+2
    #se x é inpar
    else:
        while x<=y:
            s=s+x
            print(s)
            x=x+2
           
elif y<x:
    #se y é par 
    if (y % 2) != 1:
        y=y+1
        while y<=x:
            s=s+y
            print(s)
            y=y+2
    #se y é impar
    else:
        while y<=x:
            s=s+y
            print(s)
            y=y+2
#se x e y são iguais 
else:
    print("Numeros inválidos")
