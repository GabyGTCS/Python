import Dados
import random
x=1
print("Dados Disponíveis no momento: \n D3 \n D4 \n D5 \n D6 \n D8 \n D10 \n D20 \n D100")
while x==1:
    y=int(input("Digite No de faces do dado: "))
    print("________________________")

    if y==3:
        z=Dados.d3()
    elif y==4:
        z=Dados.d4()
    elif y==5:
        z=Dados.d5()
    elif y==6:
        z=Dados.d6()
    elif y==8:
        z=Dados.d8()
    elif y==10:
        z=Dados.d10()
    elif y==20:
        z=Dados.d20()
    elif y==100:
        z=Dados.d100()
    else:
        print ("Digite um numero de faces válido!")

    print(z)
    print("________________________")
