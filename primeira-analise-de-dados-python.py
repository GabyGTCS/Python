'''
7)Implemente em Python um algoritmo que inicie uma lista com os dias da semana.
E leia, guardando em uma matriz as temperaturas que ocorreram por 3 semanas consecutivas. 
Em seguida,o algoritmo deve buscar para cada dia da semana a maior temperatura e informarem qual semana ocorreu.
    
    i --
      __________________________________________________________________________________
     |                                                                                  |
     | \   |     0    |     1    |     2    |     3    |     4    |     5    |     6    |
     |__________________________________________________________________________________|
      __________________________________________________________________________________
     |                                                                                  |
     | \   | domingo  |  segunda |  terça   |  quarta  |  quinta  |  sexta   |  sábado  |
     |__________________________________________________________________________________|
 j|  | 0   |   38.0   |   36.0   |   38.0   |   37.0   |   36.0   |   34.0   |   28.0   |
     | 1   |   36.0   |   37.0   |   37.0   |   35.0   |   37.0   |   28.0   |   28.0   |
     | 2   |   28.0   |   27.0   |   30.0   |   30.0   |   28.0   |   30.0   |   30.0   |
     |__________________________________________________________________________________|
  

            ____________________________________________________________________________
           |                                                                            |
Maior:     |   38.0   |   37.0   |   38.0   |   37.0   |   37.0   |   34.0   |   30.0   |
           |____________________________________________________________________________|
    
            ____________________________________________________________________________
           |                                                                            |
semana:    |     0    |     1    |     0    |     0    |     1    |     0    |     2    |
           |____________________________________________________________________________|

'''
D=["domingo","segunda-feira","terça-feira","quarta-feira","quinta-feira","sexta-feira","sábado"]
temp=[0.0]*3
S=[0]*7
maior=[0.0]*7
for i in range (len(temp)):
    temp[i]=[0.0]*7
    for j in range (len(temp[i])):
        temp[i][j]=float(input("Temperatura - %d semana - %s: " %((i+1),D[j])))
for i in range (len(temp(0))):
    maior[i]=temp[0][i]
    semana[i]=0
    for j in range (1,len(temp)):
        if temp[j][i] > maior[i]:
            semana[i]=j
            maior[i]=temp[j][i]
for i in range(len(temp[0])):
    print("%s - Maior temperatura é %0.2f e ocorreu na %d semana" %(dias[i],maior[i],semana[i]))