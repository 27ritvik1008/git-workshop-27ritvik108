a=list(map(int,input().split()[:3]))
b=list(map(int,input().split()[:3]))
c=[]
s=0
s1=0
for i in range(0,3):
    k=c
    if(a[i]>b[i]):
        s=s+1
k.append(s)     # APPENDING OUTSIDE THE LOOP GIVES U THE EXACT SCORE
c=k
for i in range(0,3):
    m=c
    if(b[i]>a[i]):
        s1=s1+1
m.append(s1)
c=m
print(*c)    # "*" IS FOR PRINTING WITH SPACE SEPARATION....
