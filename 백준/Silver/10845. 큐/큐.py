from collections import deque
import sys
n=int(sys.stdin.readline())
queue= deque()

for i in range(n):
    data=sys.stdin.readline().split()
    action=data[0]
    
    if action=="push":
        queue.append(data[1])
        
    elif action=="pop":
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
            
    elif action=="size":
        print(len(queue))
        
    elif action=="empty":
        if len(queue)==0:
            print(1)
        else:
            print(0)
            
    elif action=="front":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
            
    elif action=="back":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])