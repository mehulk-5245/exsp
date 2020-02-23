try:
    n=int(input())
    a=[]
    c=[]
    count=0
    for i in range(n):
        p=int(input())
        a.append(p)
    for i in range(len(a)):
        for j in range(len(a)):
            if(a[i]!=a[j]):
                if(a[i]+a[j] not in c):
                    c.append(a[i]+a[j])
                    if(str(bin(a[i]+a[j])).count("1")==1):
                        count=count+1
    print(count)          
except:
    pass    