import sys
a, b= map(int, sys.stdin.readline().split())
n=int(input())
data=list(map(int, sys.stdin.readline().split()))
data2=data[::-1]
res=[]
total=0
for i in range(n):
    total+=data2[i]*(a**i)

while total:
    res.append(total%b)
    total//=b

print(*res[::-1])