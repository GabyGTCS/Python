c = 1
p=0
while c <=6:
    x = float(input("Valor: "))
    if(x!=0):
        c=c+1
        if x>0:
            p = p+1
print("Quant. de Numeros Positivos Digitados: %d" %p)