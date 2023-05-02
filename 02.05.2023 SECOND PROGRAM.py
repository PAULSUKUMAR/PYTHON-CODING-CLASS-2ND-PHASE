l=list(map(int, input().split()))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
z=list(d.values())
x=max(z)
y=min(z)
for i in d:
    if d[i]==x:
        x=i
    if d[i]==y:
        y=i
print("MAX",x)
print("MIN",y)
print("DIFFERENCE",abs(x-y))
