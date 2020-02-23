
tc = int(input())
for i in range(tc):
    n = int(input())
    sum = 0
    while(n>=5):
        n = n//5
        sum = sum+n
    print(sum)