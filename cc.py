def check(n):
    a=[]
    i=0
    while n>0:
        a.append(n%10)
        n=n/10
        i=i+1
    k=0
    s=0
    b=[]
    for m in range(0,i):
        s=0
        for j in range(0,i):
            if(k==j):
                s=s
            else:
                s=(s*10)+a[i-j-1]
        b.append(s)
        k=k+1
    print(min(b))

nu=int(input())
a=[]
for i in range(0,nu):
    x=int(input())
    a.append(x)
for i in range(0,nu):
    check(a[i])
