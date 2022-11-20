n=int(input())

for i in range(n):
    stack=[]
    x=input()
    for j in x:
        if j == '(':
            stack.append(j)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if len(stack)==0:
            print("YES")
        else:
            print("NO")