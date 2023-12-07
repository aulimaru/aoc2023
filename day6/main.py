from math import ceil

with open("input") as file:
    input = file.read()


def solve(total, record):
    delta = (total**2 - 4*record)
    return ceil((total + delta**0.5)/2) - int((total - delta**0.5)/2) - 1


data1 = []
data2 = []
for i in input.splitlines():
    data1.append([int(j) for j in i.split(':')[1].split()])
    data2.append(int(i.split(':')[1].replace(" ", "")))

ans1 = 1
for i in range(len(data1[0])):
    ans1 *= solve(data1[0][i], data1[1][i])

ans2 = solve(data2[0], data2[1])
print(ans1)
print(ans2)
