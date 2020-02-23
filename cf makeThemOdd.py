cnt=0
z=0
a=[]
for i in range(int(input())):
    n=int(input())
    for i in range(n):
        p=int(input())
	a.append(p)
    for i in range(len(a)):
	e=a[i]
	#print(e)
        if(e%2==0):
            while(e%2==0):
                e=e//2
                z=e
	
            g=str(a)
            print(g.replace(str(e),"9"))
	
    cnt+=1
print(cnt)		
				