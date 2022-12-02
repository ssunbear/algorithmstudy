import sys
input=sys.stdin.readline
n, m=map(int, input().split())
dic={}
dic2={}

for i in range(n):
    name=input().strip()
    dic[name]=(i+1)
    dic2[i+1]=name

for i in range(m):
    action=input().strip()
    if action.isdigit()==True:
        print(dic2[int(action)])
    if action.isalpha()==True:
        print(dic[action])