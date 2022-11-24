import sys
from sys import stdin
from bisect import bisect_left, bisect_right
n=int(sys.stdin.readline())
data1=list(map(int, sys.stdin.readline().split()))
m=int(sys.stdin.readline())
data2=list(map(int, sys.stdin.readline().split()))
data1.sort()

def countbyrange(arr, value):
    rightidx=bisect_right(arr, value)
    leftidx=bisect_left(arr,value)
    return rightidx-leftidx

for i in range(len(data2)):
    print(countbyrange(data1,data2[i]), end=' ')