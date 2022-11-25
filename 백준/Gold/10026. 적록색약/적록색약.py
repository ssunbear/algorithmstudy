import sys
sys.setrecursionlimit(10001)
n= int(input())
arr1=[]
for i in range(n):
    arr1.append(list(sys.stdin.readline()))
arr2=arr1
visited1=[[0]*n for _ in range(n)]
visited2=[[0]*n for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
cnt1, cnt2=0,0

def dfs(x,y,array,visited):
    visited[x][y]=1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if array[nx][ny]==array[x][y] and visited[nx][ny]==0:
                dfs(nx,ny,array,visited)

#색맹아닌 사람
for i in range(n):
    for j in range(n):
        if visited2[i][j]==0:
            dfs(i,j,arr2,visited2)
            cnt2+=1

#색맹인 사람
for i in range(n):
    for j in range(n):
        if arr1[i][j]=='R': arr1[i][j]='G'

for i in range(n):
    for j in range(n):
        if visited1[i][j]==0:
            dfs(i,j,arr1,visited1)
            cnt1+=1

print(cnt2, cnt1)