'''
>>>AULA SOBRE VETOR<<<
No Pyton, os Vetores são denominados listas.

Calcular a média de notas de uma turma com 5 alunos

'''
notas=[0.0]*5
'''
[0.0] = quando os numeros que vamos usar são reais.
[0] = quando os numeros que vamos usar são inteiros.
[""] = quando vamos utilizar palavras.

*5= inicialização do vetor com 5 posições que possuem o valor (zero)
5= Numero de Alunos
'''
soma=0.0
i=0
while i<len(notas):
'''
i=indice do vetor
len=recebe o nome da minha lista por parametro e retorna o maior valor dela
'''
    notas[i] = float(input("Digite a nota do %d o. aluno:" %(i+1)))
    soma=soma+notas[i]
    i=i+1
media=soma/len(notas)
print ("A média da turma é %.1f" %media)
