import sys
n=int(input())
Pi=list(map(int, sys.stdin.readline().split()))
time=0
Pi.sort()
for i in range(n):
    for j in range(i+1):
        time+=Pi[j]
    
print(time)