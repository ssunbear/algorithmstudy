import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(y,x):
    if 0>x or y<0 or x>=n or y>=m:
        return False
    if graph[y][x]==1:
        graph[y][x]=0
        dfs(y,x-1)
        dfs(y,x+1)
        dfs(y-1,x)
        dfs(y+1,x)
        # 대각선 탐색
        dfs(y-1,x-1)
        dfs(y-1,x+1)
        dfs(y+1,x-1)
        dfs(y+1,x+1)
        return True    
    return False

while True:
    n,m=map(int,input().split())
    if n==0 and m==0: break    
    graph=[]
    for i in range(m):
        graph.append(list(map(int, input().split())))
    result=0
    for i in range(m):
        for j in range(n):
            if dfs(i,j)==True:
                result+=1

    print(result)