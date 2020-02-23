for i in range(int(input())):
	x,y,z = sorted(map(int,input().split()))
	print(max(0,2*(z-x)-4))