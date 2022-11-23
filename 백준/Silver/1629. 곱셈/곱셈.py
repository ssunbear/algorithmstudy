import sys
a, b, c= map(int, sys.stdin.readline().split())
#분할정복의 아이디어 
def DaC(a, b):
    if b==1:
        return a%c

    tmp=DaC(a, b//2)

    if b%2==0:
        return tmp*tmp%c
    else:
        return tmp*tmp*a%c

print(DaC(a,b))