m=[0]*3
print("digita ae do 5 ao 13" )
for i in range(len(m)):
    m[i]=[]
    for j in range(3):
        m[i].append(int(input()))
print(m)        
for i in range(len(m)):
    x=m[i][0]
    t=len(m[0])-1
    for j in range(t):
        m[i][j]=m[i][j+1]
    m[i][t]=x
print(m)