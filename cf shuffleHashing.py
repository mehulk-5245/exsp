for _ in range(int(input())):
    a=sorted(input())
    b=input();ans="NO"
    for i in range(len(b)-len(a)+1):
        if sorted(b[i:i+len(a)])==a:
            ans="YES";break;
    print(ans)