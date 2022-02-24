'''
O comando "import" para importar uma função que está na biblioteca principal do python.

"def "nome da função"() - Define função... tipo... ele meio que nomeia um conjunto de processos pra gente n ter q ficar 
redigitando eles

Pra gente chamar essa função a gente apenas digita ela:
Ex:

def mensagem1():
    print ("Olá")

Determinar função principal, a gente geralmente usa "main" 

Para criar sua prorpia biblioteca basta criar uma nova aba e referenciá-la neste documento. Traduzindo usando o "import"

sempre quando vc quer referenciar uma função no meio de um codigo vc deve primeiro digitar o nome da biblioteca 
(no caso minhasfuncoes) o ponto e o nome da função (no caso mensagem3()). então fica: minhasfuncoes.mensagem3

'''
import minhasfuncoes

def main():
    print(minhasfuncoes.mensagem3())
    x=minhasfuncoes.mensagem3()
    minhasfuncoes.mensagem2()

#função ja foi definida no minhasfuncoes.py agora vamos ao calculo

x=22
y=int(input("Ditite seu ano de nascimento (sem abreveações): "))
main()