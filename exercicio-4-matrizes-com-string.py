'''

Implemente em Python um algoritmo que leia strings para uma matriz quadrada de ordem 2.
Em seguida mostre os elementos da diagonal principal.
O End evita que o proximo print va para a proxima linha... os 2 ficam na mesma
(Ele Funciona ao contrário do "\ n" )

'''
m=[""]*2
for i in range (len(m)):
    m[i]=[""]*2
    for j in range (len(m[i])):
        m[i][j]=input("Digite uma palavra: ")
print ("Elementos da diagonal principal: ", end="")
for i in range (len(m)):
    print("%s" %m[i][i], end="")
