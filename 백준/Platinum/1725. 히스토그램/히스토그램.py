n = int(input())
result = 0
s = []
data = []

for i in range(n):
    data.append(int(input()))

#왼쪽부터 검사
for i in range(n):
    while s and data[s[-1]] > data[i]:
        height = data[s[-1]]
        s.pop()
        width = i
        #4 5 1 같은 경우 5 pop 후 4 -> 너비 2만들기 위해
        if s:
            width = (i - s[-1] - 1)
        result = max(result, width * height)
    s.append(i)

#스택에서 오른쪽 높이부터 검사
while s:
    height = data[s[-1]]
    s.pop()
    width = n
    if s:
        width = (n - s[-1] - 1)
    result = max(result, width * height)

print(result)