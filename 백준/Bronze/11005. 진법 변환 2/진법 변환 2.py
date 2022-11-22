import sys
d=[]
dchar="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n,b= map(int,sys.stdin.readline().split())
while n>0:
    d+=dchar[n%b]
    n//=b

print("".join(d[::-1]))
