def sod(q):
    sum=0 
    while(q!=0):
        sum=sum+(q%10)
        q=q//10
    return sum    

n=int(input())
p=0
while(p!=1):
    if(sod(n)%4==0):
        print(n)
        p=1
    else:
        n=n+1        