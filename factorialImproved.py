import math as m
n=int(input())
f=[]
count=0
for i in range(n):
    a=int(input())
    b=m.factorial(a)
    c=str(b)
    f.append(c)
for i in range(len(f)):
    t=f[i]
    d=len(t)
    for i in range(d):
        if(t[d-i-1]=="0"):
            count=count+1
        else:
            break    
    print(count)    
