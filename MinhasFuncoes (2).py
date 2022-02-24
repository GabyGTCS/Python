import ramdom

def tabuada(n):
    s=""
    for i in range (11):
        res = n * i
        s= s + str (n) + "x" +str(i) + " = " + str(res) + "\n"
    return s
def soma(n1,n2):
    return n1+n2
    
def subtrai(n1,n2):
    return n1-n2

def multiplica (n1,n2):
    return n1*n2
    
def divide (n1,n2):
    return n1/n2