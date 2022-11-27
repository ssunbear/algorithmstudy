import sys
sys.setrecursionlimit(10**7)
from collections import deque
n,m=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for i in range(m):
    u,v=map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    graph[i].sort()

def dfs(graph, u, visited):
    if visited[u]>0:
        return
    visited[u]=1
    for i in graph[u]:
        dfs(graph, i, visited)

cnt=0
for i in range(1,n+1):
    if visited[i]==0:
        cnt+=1
        dfs(graph, i , visited)

print(cnt)