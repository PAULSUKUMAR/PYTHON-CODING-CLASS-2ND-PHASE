l=[]
n=int(input("Enter length of the list"))
for i in range(1,n+1):
	num=int(input())
	l.append(num)
print(l)
x=max(l)
y=min(l)
z=x-y
print("MAX ELE",x)
print("MIN ELE",y)
print("DIFF IS",z)

