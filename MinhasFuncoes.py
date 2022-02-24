def mostrarElementos(lista):
    for i in range (len(lista)):
        lista [i]*=2
        print (lista[i])

def serie1 (n):
    d=3
    s=0
    while d<=n:
        s = s +1/d
        d = d * 3
    return s