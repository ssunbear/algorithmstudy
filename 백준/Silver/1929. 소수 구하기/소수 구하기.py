import sys

def isPrime(N):
    if N==1: return False
    for i in range(2,int(N**0.5)+1):
        if N % i==0: return False
    return True


a,b=map(int, sys.stdin.readline().split())
for i in range(a, b+1):
    if isPrime(i)==1:
        print(i)