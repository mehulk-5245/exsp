try:
    n=int(input())
    for i in range(n):
        s=raw_input()              #input() for cf
        l=len(s)-2
        if(len(s)>10):
            print(s[0]+str(l)+s[len(s)-1])
        else:
            print(s)    
except:
    pass