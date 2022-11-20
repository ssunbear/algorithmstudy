import sys
stack=[]
n=int(input())

for i in range(n):
    word=sys.stdin.readline().split()
    action=word[0]
    if action == "push":
        stack.append(word[1])
    elif action == "top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[len(stack)-1])
    elif action == "pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[len(stack)-1])
            stack.pop()
    elif action =="size":
        print(len(stack))
    elif action =="empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
