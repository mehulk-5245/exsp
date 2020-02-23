a=[]
b=[]
cnt=0
j=0
for i in range(int(input())):
    s,c=input().split()
    if((s not in a) and (c not in b)):
        a.append(s)
        b.append(c)
        cnt=cnt+1
    elif((s in a) and (c not in b)):
        a.append(s)
        b.append(c)
        cnt=cnt+1
    elif((s not in a) and (c in b)):
        a.append(s)
        b.append(c)
        cnt=cnt+1    
    else:
        j=1
print(cnt+1)        
            
            
        