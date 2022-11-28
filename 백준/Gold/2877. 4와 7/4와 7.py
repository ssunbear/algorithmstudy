n=int(input())
x=format(n+1, 'b')
x=x[1::]
res=''
for i in range(len(x)):
    if x[i]=='0':
        res+='4'
    else:
        res+='7'

print(res)
