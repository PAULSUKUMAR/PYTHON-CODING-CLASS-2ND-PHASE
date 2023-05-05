import math
seive=[]
n=int(input("Enter n value:"))
n=n+1
x=int(math.sqrt(n))
for i in range(0,n):
    seive.append(1)
for i in range(2,x+1):
    if seive[1]==1:
        for j in range(i*i,n,i):
            seive[j]=0
count=0
for i in range(2,n):
    if seive[i]==1:
        count+=1
print("count of all prime numbers upto",n-1,"are:",count)
