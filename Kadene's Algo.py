#Kadene's Algo
for i in range(int(input())):
    n = int(input())
    w = list(map(int,input().split()))
    meh,msf = 0,min(w)
    for j in range(n):
        meh = meh + w[j]
        #print(meh)
        if(meh < w[j]):
            meh = w[j]
        if(msf < meh):
            msf = meh
    print(msf)            
