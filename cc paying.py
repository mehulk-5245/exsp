# cook your dish here
from itertools import combinations
for _ in range(int(input())):
    n, m = map(int, input().split())
    l1 = [int(input()) for i in range(n)]
    bool1 = False
    for i in range(1, len(l1) + 1):
        l2 = list(combinations(l1, i))
        for j in l2:
            #print(j)
            if sum(list(j)) == m:
                bool1 = True
                break
            else:
                bool1 = False
        if bool1:
            print("Yes")
            break
    if bool1 == False:
        print("No")