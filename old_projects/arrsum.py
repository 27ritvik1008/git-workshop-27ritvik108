b=int(input())
s=0
a=list(map(int,input().split()[:b]))
for i in range(0,b):
	s=s+a[i]
print(s)
	
