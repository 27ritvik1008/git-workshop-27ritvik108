a=int(input())
i=0
rev=0
while(a>=0):
	k=a	
	a=a%10
	rev=(rev*10)+a
	k=k//10
	a=k
print(rev)

