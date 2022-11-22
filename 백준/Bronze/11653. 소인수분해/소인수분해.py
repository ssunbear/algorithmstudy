import sys
n=int(sys.stdin.readline())
if n==1: exit
n1=n
for i in range(2, n1+1):
    if n%i==0:
        while n%i==0:
            n//=i
            print(i)
    if n==1: break