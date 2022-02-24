N=int(input("Digite o valor de 'N': "))
n=1
if N>1:
  #se é par
  if (N%2)!=1:
    n=n+1
    while n<=N:
      print (n)
      n=n+2
  #se é ímpar
  else:
    N=N-1
    n=n+1
    while n<=N:
      print (n)
      n=n+2
else:
  #se é par
  if (N%2)!=1:
    N=N+1
    while N<=n:
      print (N)
      N=N+2
  #se é ímpar    
  else:   
    while N<=n:
      print (N)
      N=N+2