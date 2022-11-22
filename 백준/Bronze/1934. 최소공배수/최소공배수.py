import sys
import math
n=int(input())
res=[]
for i in range(n):
    A,B=map(int, sys.stdin.readline().split())
    res.append(math.lcm(A,B))

for i in res:
    print(i)