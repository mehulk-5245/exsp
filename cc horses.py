try:
    h=[]
    n=0
    p=0
    n=int(input()) 
    p=int(input())
    for i in range(n):
        a=(raw_input().split(" "))
    #for i in range(n):
        for j in range(p):
            for k in range(p):
                if(a[j]!=a[k]):
                    h.append(abs(int(a[j])-int(a[k])))
        print(min(h))
    del(h[:])
               
except:
    pass