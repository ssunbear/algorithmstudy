import sys
input = sys.stdin.readline

a, p=input().split()
A=[]
A.append(int(a))
cnt=1
while True:
    num, i=0, 0
    while i<len(a):
        num+=int(a[i])**int(p)
        i+=1
    a=(str(num))
    if num in A:
        print(A.index(num))
        break
    else:
        A.append(num)