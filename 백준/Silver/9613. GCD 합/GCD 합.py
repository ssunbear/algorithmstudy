import sys
import math

n=int(input())
res=[]
for i in range(n):
    data = list(map(int,sys.stdin.readline().split()))
    total=0
    for j in range(1,data[0]+1):
        for k in range (j+1, data[0]+1):
            total+=math.gcd(data[j],data[k])
    res.append(total)

for i in res:
    print(i)