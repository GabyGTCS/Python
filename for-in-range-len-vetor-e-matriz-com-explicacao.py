'''
[0] = Cria uma linha com 0
*3 = Multiplica essa linha em 3 vezes
Logo fica: [0],[0],[0]
ou
m1:
    [0]
    [0]
    [0]
for x = para x
in range (y)= sendo até (y) (ele gera valores de 0 até o valor total menos 1,
então se y é igual a 3, o in range gera valores de 0 até 2)
len = Pega a largura total da linha (ou coluna, ou matriz)

i = neste algoritmo simboliza a linha
j = neste algoritmo simboliza a coluna

O Python identifica i como linha e o j como coluna por causa do 
"[i] [j]" (O Python identifica altomaticamnte que o valor que ta 
no primeiro couchete é linha e o que ta no segundo couchete é coluna)

'''
m1=[0]*3
m2=[0]*3
'''Esses primeiros valores criam o numero de **Linhas** para cada Matriz'''

for i in range (len(m1)):
    for j in range (len(m1)):
        m1 [i] = [0]*3
        m2 [i] = [0]*3
        '''Esses segundos valores criam o numero de **Colunas** para cada Matriz'''
        
        for j in range (len(m1[i])):
            m1 [i] [j]= i+2
            m2 [i] [j]= j+2
print (m1)
print (m2)
print ("---------------------------------")
for i in range (len(m1)):
    for j in range(len(m1)):
        if m1 [i][j]==m2 [i][j]:
            m1[i][j] = 0
        else:
            m2[i][j]=1
print (m1)
print (m2)

'''
logo fica a logica fica:
    _____________________________________________
   |                                             |
   | i   |   j   |   m1 [i][j]   |   m2[i][j]    |
   |_____________________________________________|
   | 0   |   0   |   2           |   2           |
   | 0   |   1   |   2           |   3           |
   | 0   |   2   |   2           |   4           |
   |_____________________________________________|
   | 1   |   0   |   3           |   2           |
   | 1   |   1   |   3           |   3           |
   | 1   |   2   |   3           |   4           |
   |_____________________________________________|
   | 2   |   0   |   4           |   2           |
   | 2   |   1   |   4           |   3           |
   | 2   |   2   |   4           |   4           |
   |_____________________________________________|    
    
_____________________________________________________
    
    _____________________________________________
   |                                             |
   | i   |   j   |   m1 [i][j]   |   m2[i][j]    |
   |_____________________________________________|
   | 0   |   0   |   0           |   2           |
   | 0   |   1   |   2           |   1           |
   | 0   |   2   |   2           |   1           |
   |_____________________________________________|
   | 1   |   0   |   3           |   1           |
   | 1   |   1   |   0           |   3           |
   | 1   |   2   |   3           |   1           |
   |_____________________________________________|
   | 2   |   0   |   4           |   1           |
   | 2   |   1   |   4           |   1           |
   | 2   |   2   |   0           |   4           |
   |_____________________________________________|
    
    
    
    
