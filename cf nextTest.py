a=[]
p=1
b=1
for i in range(int(input())):
    p=map(int,raw_input().split(" "))
for i in range(len(p)):
    a.append(p[i])
while(b!=0):
    if p in a:
        p=p+1
    else:
        print(p)
        b=0       