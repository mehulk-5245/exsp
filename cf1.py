import math as m
def prime(l):
     for i in range(2,l):                                                           #for i in range(2,int(m.sqrt(l)/2)):
        if(l%i==0):
            return 1
        else:
            return 0    

n=int(input())
p=0
a=3
b=1
while(p==0):
    u=prime(a)
    v=prime(b)
    if(u==0 and v==0):
        if(a-b==n):
            print(a)
            print(b)
            p=1
    else:
        a=a+1
        b=b+1   
                
                   
                   
            
        
     