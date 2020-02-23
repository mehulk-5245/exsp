a=[]
b=[]
c=[]
for i in range(int(input())):
    x,y,z=map(int,input().split())
    a.append(x)
    b.append(y)
    c.append(z)
if(sum(a)==0 and sum(b)==0 and sum(c)==0):
    print("YES")
else:
    print("NO")        