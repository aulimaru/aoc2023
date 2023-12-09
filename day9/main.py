with open("input") as file:
    input = file.read()
data = []
for i in input.splitlines():
    data.append([int(i) for i in i.strip('\n').split()])


def isend(s):
    for i in s:
        if i != 0:
            return False
    return True


def nexts(s):
    for i in range(len(s)-1):
        s[i] = s[i+1]-s[i]
    return s[:len(s)-1]


ans1 = 0
ans2 = 0
for i in data:
    firstnumbers = []
    while not isend(i):
        ans1 += i[len(i)-1]
        firstnumbers.append(i[0])
        i = nexts(i)
    r2 = 0
    for i in firstnumbers[::-1]:
        r2 = i - r2
    ans2 += r2
print(ans1)
print(ans2)
