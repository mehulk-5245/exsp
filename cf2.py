a=[]
b=0
n=int(input())
for i in range(n):
    s=input()
    a.append(s)
for i in range(n):
    t=a[i]
    b=len(t)
    if(t[b-1]=="o" and t[b-2]=="p"):
        print("FILIPINO") 
    if(t[b-1]=="u" and t[b-2]=="s" and (t[b-3]=="e" or "a") and (t[b-4]=="d" or "m")):
        print("JAPANESE")
    if(t[b-1]=="a" and t[b-2]=="d" and t[b-3]=="i" and t[b-4]=="n" and t[b-5]=="m"):
        print("KOREAN")    
                
           