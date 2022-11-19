n=list(input())
count=0
flag=0
for i in n:
    if int(i)== 0:
        flag=1
    count+=int(i)

n.sort(reverse=True)
    
if count%3==0 and flag==1:
    print(''.join(n))
else:
    print(-1)
