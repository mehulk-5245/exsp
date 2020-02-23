for i in range(int(input())):
    h,m=map(int,raw_input().split(" "))          #input() and split() for cf
    if(h>=23):
        print(60-m)
    else:
        p=((24-h-1)*60)+(60-m)
        print(p)    
    