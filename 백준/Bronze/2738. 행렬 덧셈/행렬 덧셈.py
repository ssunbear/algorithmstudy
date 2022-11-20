import sys

n,m = map(int,sys.stdin.readline().split())

array1=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
array2=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(array1[i][j] + array2[i][j], end=' ')
    print()