import sys
n , k= map(int, sys.stdin.readline().split())
a=[0]*n
suma=[0]*n
data=list(map(int, sys.stdin.readline().split()))
def something(jump, cnt):
    i=0
    while i<n:
        a[i]=a[i]+cnt
        i+=jump
data2=dict()
for i in data:
    if i in data2: data2[i]+=1
    else: data2[i]=1
list1=list(data2.keys())
list2=list(data2.values())
for i in range(len(data2)): something(list1[i],list2[i])
#누적합 계산으로 시간복잡도 및 메모리공간 확보
suma[0]=a[0]
for i in range(1,n): suma[i]=suma[i-1]+a[i]
for i in range(int(sys.stdin.readline())):
    l, r =map(int, sys.stdin.readline().split())
    if(l!=0): print(suma[r]-suma[l-1])
    else: print(suma[r])