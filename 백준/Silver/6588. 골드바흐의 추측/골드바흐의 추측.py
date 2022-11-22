#에라토스테네스의 체 공부하기
import sys
a=[True  for i in range(1000001)]
for i in range(2,1001):
    if a[i]:
        for j in range(2*i,1000001,i):
            a[j]=False
        
while True:
    n=int(sys.stdin.readline())
    if n==0: break
    for i in range(3, len(a)):
        if a[i] and a[n-i]:
            print(n, "=", i , "+", n-i)
            break