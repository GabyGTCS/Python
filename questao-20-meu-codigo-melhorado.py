'''

Leia 2 valores inteiros X e Y. A seguir, calcule e mostre 
a soma dos números impares entre eles.

'''
n=1
while n==1:
    x=int(input("insira valor X: "))
    y=int(input("insira valor Y: "))
    s=0
    if x<y and (x % 2) == 1:
        while x<=y:
            s=s+x
            x=x+2

    elif x<y and (x % 2) != 1:
        x=x+1
        while x<=y:
            s=s+x
            x=x+2
           
    elif y<x and (y % 2) == 1:
        while y<=x:
            s=s+y
            y=y+2
    elif y<x and (y % 2) != 1:
        y=y+1
        while y<=x:
            s=s+y
            y=y+2
    else:
        print("Numeros são iguais. Por favor, verifique se digitou o intervalo corretamente.")
    print(s)
    n=int(input("Digite 1 para recomeçar\nDigite 2 para finalizar\n"))
    if n<1 or n>2:
        print ("Erro de sintaxe. Por favor, digite um numero valido.")
    elif n==2:
        print("Sessão finalizada com Sucesso. Aperte 'Enter' para sair.")

