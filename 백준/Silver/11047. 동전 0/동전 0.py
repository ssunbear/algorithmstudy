import sys
n, k = map(int, sys.stdin.readline().split())
coin=[]

for i in range(n):
    type=int(input())
    coin.append(type)
cnt=0
coin.sort(reverse=True)

for i in coin:
    if k>=i:
        cnt+=k//i
        k-=i*(k//i)

print(cnt)