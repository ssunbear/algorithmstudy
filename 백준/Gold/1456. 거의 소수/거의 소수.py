import sys
import math

a, b= map(int, sys.stdin.readline().split())
c=int(math.sqrt(b))+1

x=[True]*(c)
x[1]=False
for i in range(2,c):
    if x[i]:
        if i**2 >c: break
        for j in range(i*i, c, i):
            x[j]=False

count=0
for i in range(1,len(x)):
    if x[i]:
        res=i**2
        while True:
            if res < a:
                res *= i
                continue
            if res>b:
                break
            res*=i
            count+=1

print(count)