import MinhasFuncoes
def main():
    n=1
    while n<3:
        n =int(input("Valor (a partir de 3): "))
    serie = MinhasFuncoes.serie1(n)
    
    print("Resultado: ", serie)