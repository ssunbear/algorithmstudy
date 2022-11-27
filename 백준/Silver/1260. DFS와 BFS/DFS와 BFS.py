import sys
from collections import deque
n,m,v=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    x,y=map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1,n+1):
    graph[i].sort()

visited=[False]*(n+1)
visited1=[False]*(n+1)
def dfs(graph, u, visited):
    visited[u]=True
    print(u, end=' ')
    for i in graph[u]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, u, visited1):
    queue=deque([u])
    visited1[u]=True
    
    while queue:
        v1=queue.popleft()
        print(v1, end=' ')
        for i in graph[v1]:
            if not visited1[i]:
                queue.append(i)
                visited1[i]=True

dfs(graph,v,visited)
print()
bfs(graph, v , visited1)