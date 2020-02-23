try:
    count=0
    for i in range(int(input())):
        a,b,c=input().split()
        if((a=="1" and b=="1") or (a=="1" and c=="1") or (c=="1" and b=="1") or (a=="1" and b=="1" and c=="1")):
            count=count+1
    print(int(count))
except:
    pass    