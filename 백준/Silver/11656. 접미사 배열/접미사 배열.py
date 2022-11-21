s=input()
data=[]
for i in range(len(s)):
    data.append(s[i::1])

data.sort()

for i in range(len(s)):
    print(data[i])