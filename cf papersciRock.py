f=input()
m=input()
s=input()
if(f=="paper"and m==s=="rock"):
    print("F")
elif(m=="paper"and f==s=="rock"):
    print("M")
elif(s=="paper"and m==f=="rock"):
    print("S")
elif(f=="scissors"and m==s=="paper"):
    print("F")
elif(m=="scissors"and f==s=="paper"):
    print("M")
elif(s=="scissors"and m==f=="paper"):
    print("S")
elif(f=="rock"and m==s=="scissors"):
    print("F")
elif(m=="rock"and f==s=="scissors"):
    print("M")
elif(s=="rock"and m==f=="scissors"):
    print("S") 
else:
    print("?")          
       