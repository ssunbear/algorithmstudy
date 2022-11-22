import sys
import math

A,B=map(int, sys.stdin.readline().split())
print('1'*math.gcd(A,B))
#유클리드 호제법 공부 