import sys
n, m, k = map(int, sys.stdin.readline().split())
team=0
people=n+m

while True:
    if people -3>=k and n>=2 and m>=1:
        team+=1
        n,m,people=n-2,m-1,people-3
    else:
        print(team)
        break