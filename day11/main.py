with open("input") as file:
    input = file.read()

data = []
for i in input.splitlines():
    data.append([j for j in i.strip('\n')])

rows = []
cols = []
for i in range(len(data)):
    if '#' not in data[i]:
        rows.append(i)
for i in range(len(data[0])):
    flag = True
    for j in range(len(data)):
        if data[j][i] == '#':
            flag = False
    if flag:
        cols.append(i)


points = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '#':
            points.append([i, j])


def position(s, x):
    i = 0
    while i < len(s) and s[i] < x:
        i += 1
    return i


def distance(a, b, step):
    r = 0
    r += abs(position(rows, a[0])-position(rows, b[0])) * (step - 1)
    r += abs(position(cols, a[1])-position(cols, b[1])) * (step - 1)
    r += abs(a[0]-b[0]) + abs(a[1]-b[1])
    return r


ans1 = 0
ans2 = 0
for i in range(len(points)):
    for j in range(i+1, len(points)):
        ans1 += distance(points[i], points[j], 2)
        ans2 += distance(points[i], points[j], 1000000)

print(ans1)
print(ans2)
