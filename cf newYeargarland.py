t=int(input())
for _ in range(t):
	r,g,b=sorted(map(int,raw_input().split(" ")))
	print("No" if b>g+r+1 else "Yes")