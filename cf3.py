a=[]
b=9
count=0
n=int(input())
for i in range(n):
    y=int(input())
    a.append(y)
for i in range(n):
    t=a[i]
    l=len(str(t))
    if(l==1):
        print(t)
    else:
        for i in range(10,t):
            p=str(i)
            w=p[1]
            
            for j in range(0,len(p)):
                if(p[j]==w):
                    count=(count+2)
                    count=count-len(p)
        print(b+count)            
            
---------------------------------------------------------------------------------            
a=[]
b=5
count=0
n=int(input())
for i in range(n):
    y=int(input())
    a.append(y)
for i in range(n):
    t=a[i]
    l=len(str(t))
    if(l==1):
        print(t)
    else:
        for i in range(10,t):
            p=str(i)
            w=p[1]
            
            for j in range(0,len(p)):
                if(p[j]==w):
                    
                    count=count+2
                count=count-1    
        count=count-1       
        
        print(b+count)            
            
            
       