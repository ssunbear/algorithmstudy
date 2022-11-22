import sys

def isPrime(N):
    if N==1: return False
    for i in range(2,N):
        if N % i==0: return False
    return True

n=int(input())
data=list(map(int, sys.stdin.readline().split()))
cnt=0
for i in data:
    if isPrime(i)==1:
        cnt+=1

print(cnt)