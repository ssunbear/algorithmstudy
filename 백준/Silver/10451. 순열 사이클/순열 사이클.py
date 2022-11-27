import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(v):
    visited[v]=1
    if visited[graph[v]]==0:
        dfs(graph[v])

K = int(input())
for _ in range(K):
    cnt=0
    V=int(input())
    visited = [0] * (V+1)
    graph=[0]+list(map(int, input().split()))


    for i in range(1, V+1):
       if visited[i] == 0: # 방문하지 않은 정점이면 dfs 수행
            cnt+=1 
            dfs(i)        
    print(cnt)