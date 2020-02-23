
for i in range(int(input())):
    n,k=map(int,raw_input().split())
    w=list(map(int,raw_input().split()))
    w.sort()
    k=min(k,n-k)
    print(sum(w[k:])-sum(w[:k]))
    
    
   
                  
        
                        