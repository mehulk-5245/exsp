try:
    v,w=raw_input().split()
    n=int(v)
    k=int(w)
    count=0
    a=[]
    for i in range(n):
        p=int(input())
        if(p>0):
            a.append(p)
    for i in range(len(a)):
        if(a[i]>=a[k-1]):
            count=count+1    
    print(count) 
except:
    pass           
        