
try:
    g,h,j=input().split()
    n=int(g)
    m=int(h)
    a=int(j)
    b=2
    p=0
    while(p==0):
        if(((a*a)*b)>=(n*m)):
            print(b)
            p=1
        else:
            b=b+2
except:
    pass
            
    
    
    
