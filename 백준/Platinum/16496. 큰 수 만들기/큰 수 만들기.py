import sys
n=int(sys.stdin.readline())
data=list(map(int, sys.stdin.readline().split()))
a=[]
b=''
cnt=0
maxlen=0
for i in range(n):
    if maxlen<=len(str(data[i])): maxlen=len(str(data[i]))
    if data[i]==0:
        cnt+=1
maxlen=2*maxlen        
for i in range(n):
    a.append([(str(data[i]) * (maxlen // len(str(data[i])) + 1))[:maxlen], len(str(data[i]))])
     
if cnt==n:
    print(0)
else:
    a.sort(reverse=True)
    for i in range(n):
       b+=a[i][0][:a[i][1]]
    print(int(b))
