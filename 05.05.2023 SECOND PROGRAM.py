import math
seive=[]
n=int(input("Enter n value:"))
n=n+1
x=int(math.sqrt(n))
for i in range(0,n):
      seive.append(1)
for i in range(2,x+1):
      if seive[i]==1:
          for j in range(i*i,n,i):
              seive[j]=0
sum=0
for i in range(2,n):
      if(seive[i]==1):
          sum=sum+i
print("sum of prime numbers upto ",n-1,"are:",sum)
