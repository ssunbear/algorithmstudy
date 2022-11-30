import sys, math
n=int(sys.stdin.readline())
dp=[0,1]+[0]*(n-1)

for i in range(2,n+1):
    res, j=1e9, 1
    while j**2<=i:
        res=min(res, dp[i-j**2])
        j+=1
    dp[i]=res+1

print(dp[n])