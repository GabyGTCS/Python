def gravarA(nome, texto):
    arq = open(nome, 'w')
    arq.write(texto)
    arq.close()

def gravarB(nome, texto):
    arq = open(nome, 'a')
    arq.write(texto)
    arq.close()
    
def lerA(nome):
    arq = open(nome, 'r')
    texto = arq.read()
    arq.close()
    return texto

def lerB(nome):
    arq = open(nome, 'r')
    texto = arq.readlines()
    lista = []
    for linha in texto :
        lista.append(linha)
    arq.close()
    return lista

def main():
    lista1 = [["Beatriz",15], ["Cilene",78], ["Marcos",55], ["Zileide", 40]]
    for pessoa in lista1:
        t = "Nome completo " + pessoa[0] + " - Pontos " + str(pessoa[1]) + '\n' 
        gravarA("arquivo1.txt", t)
        gravarB("arquivo2.txt", t)
    t = lerA("arquivo2.txt")
    lista2 = lerB("arquivo2.txt")
    print ("Leitura pela funcao lerA: ", t)
    print ("Leitura pela funcao lerB: ", lista2)

main()