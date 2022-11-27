import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n= int(input())

Tree=[[] for _ in range(n+1)]
parents=[0 for _ in range(n+1)]

for _ in range(n-1):
    a, b= map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)

def DFS(start):
    for i in Tree[start]:
        if parents[i]==0:
            parents[i]=start
            DFS(i)

DFS(1)
for i in range(2,n+1):
    print(parents[i])