for i in range(int(input())):
    n,s = map(int,input().split())
    w = list(map(int,input().split()))
    cus=0
    p=0
    ma={}
    for j in range(n):
        cus+=w[j]
        if(cus==s):
            print(1,j+1)
            p=p+1
            break
        if((cus-s) in ma):
            print(ma[cus-s]+1,j+1)
            p=p+1
            break
        ma[cus]=j+1
    if(p==0):
        print(-1)
        
