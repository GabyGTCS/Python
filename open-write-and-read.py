f=open("arquivo.txt","w")
f.write("olá!")
f.close()

f=open("arquivo.txt","r")
print(f.read())
f.close()