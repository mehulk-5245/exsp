for _ in[0]*int(input()):
 s,c=input().split();t=sorted(s);i=0;l=len(s)
 while i<l and s[i]==t[i]:i+=1
 if i<l:j=s.rfind(t[i]);s=s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
 print(('---',s)[s<c])
