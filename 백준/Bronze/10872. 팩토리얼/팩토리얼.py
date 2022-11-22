def factorial(n):
    if n>0:
        return n*factorial(n-1)
    else: return 1

import sys
n=int(sys.stdin.readline())
print(factorial(n))