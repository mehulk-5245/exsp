a=[]
b=[]
n=int(input())
for i in range(n):
    s=raw_input()
    a.append(s)
for i in range(n):
    t=a[i]
    b=len(t)
    for i in range(b):
        b.append(t[i])
        if(b[i]!=b[i+1]):
            print(b[i])
                