def makeprime(n):
    a=[False, False] + [True]*(n)
    
    for i in range(2,n+1):
        if a[i]:
            for j in range(2*i, n+1, i):
                a[j]=False

    return a

n=int(input())
answer=''
if n<8:
    print(-1)
elif n%2==1:
    answer = "2 3 "
    n-=5
else:
    answer = "2 2 "
    n-=4

prime = makeprime(n)

for i in range(2, n+1):
    if prime[i] and prime[n-i]:
        answer+= str(i) + ' ' + str(n-i)
        print(answer)
        break
