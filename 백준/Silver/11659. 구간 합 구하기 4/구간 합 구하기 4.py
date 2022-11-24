import sys
n, m = map(int, sys.stdin.readline().split())
array=list(map(int, sys.stdin.readline().split()))
sumarray=[0]*(n+1)
for i in range(1,n+1):
    sumarray[i]=sumarray[i-1]+array[i-1]

for i in range(m):
    r, w= map(int, sys.stdin.readline().split())
    print(sumarray[w]-sumarray[r-1])