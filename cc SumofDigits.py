try:
    sum=0
    b=[]
    a=int(input())
    for i in range(a):
        n=int(input())
        b.append(n)
    for i in range(len(b)):
        q=b[i]    
        while(q!=0):
            sum=sum+(q%10)
            q=q//10
        print(sum)
        sum=0
except:
    pass        
    
    
    
    
    
    
    
    def calc(e,r,t,o,cn): 
	try:	
		e=e+t
		r=r-o
    	cn+=1
    	if(e==r)
    		print(cn)
    	elif(e>r)
       		print(-1) 
    	else
       		calc(e,r,t,o,cn)
	except:pass    	
try:        
	for i in range(int(input())):
    	x,y,a,b=map(int,input().split())
    	cnt=0
    	calc(x,y,a,b,cnt)
except:pass    	