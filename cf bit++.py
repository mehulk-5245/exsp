x=0
for i in range(int(input())):
    s=input()
    if(s=="X++"):
        x=x+1
    elif(s=="++X"):
        x=x+1
    elif(s=="--X"):
        x=x-1
    else:
        x=x-1              
print(x)