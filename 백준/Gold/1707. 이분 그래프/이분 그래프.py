from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = 1 

    while queue:
        v = queue.popleft()
        for i in graph[v]: 
            if visited[i] == 0:
                queue.append(i)
                visited[i] = -visited[v]
            elif visited[i] == visited[v]: # 이미 방문한 정점이 같은 그룹이라면 False
                return False
    return True

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)] 
    visited = [0] * (V+1) 
    result = True 

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V+1):
        if visited[i] == 0: # 방문하지 않은 정점이면 bfs 수행
            if not bfs(i): # 이분 그래프가 아니라면 탐색 중단
                result = False
                break
    print('YES' if result else 'NO')
