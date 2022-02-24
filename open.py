f=open("Um teste.txt","r")
texto=f.read().split("\n")
f.close()
lista = []
for i in range (len(texto)):
    lista.append(texto[i].split(" "))
print(lista)
print(texto)