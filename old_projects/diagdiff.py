a=int(input())
l=[]
sum1=0
sum2=0
for i in range(a):
    row=input().split()
    for i in range(len(row)):
        row[j]=int(row[j])
    l.append(row)
for i in range(a):
    for j in range(a):
        if(i==j):
            sum1 = sum1 + l[[i][j]]
        if(abs(i-j)==a-1):
            sum2 = sum2 + l[[i][j]]
        if(a>2):
            if(i==a-1 and j==a-1):
                sum2 =sum2 + l[[i][j]]
print(abs(sum2-sum1))       
