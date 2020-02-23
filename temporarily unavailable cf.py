n=int(input())
for i in range(n):
    a,b,c,r=map(int,input().split())
    s=min(a,b)
    l=max(a,b)
    if (s<=c-r and l<=c-r) or (s>=c+r and l>=c+r):
        result=abs(l-s)
    elif s<=c-r and l>=c-r and l<=c+r:
        result=abs(c-r-s)
    elif s>=c-r and s<=c+r and l>=c+r:
        result=abs(l-c-r)
    elif s>=c-r and s<=c+r and l>=c-r and l<=c+r:
        result=0
    else:
        result=abs(c-r-s)+abs(l-r-c)
    print(result)
 