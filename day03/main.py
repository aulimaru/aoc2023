pos = [[-1, 0], [-1, 1], [-1, -1], [0, -1], [0, 1], [1, 1], [1, 0], [1, -1]]

with open("input") as file:
    input = file.read()
lines = [list(i) for i in input.splitlines()]


def parse(linen, x):
    global lines
    while x >= 0 and '0' <= lines[linen][x] <= '9':
        x -= 1
    r = ""
    if x < 0:
        x = 0
    else:
        x += 1
    while x < len(lines[linen]) and '0' <= lines[linen][x] <= '9':
        r += lines[linen][x]
        lines[linen][x] = '.'
        x += 1
    return int(r)


ans1 = 0
ans2 = 0


for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        if lines[i][j] != '.' and not lines[i][j].isdigit():
            numbers = []
            for k in pos:
                if len(lines) > i+k[0] >= 0 and len(lines[i]) > j+k[1] >= 0 and '0' <= lines[i+k[0]][j+k[1]] <= '9':
                    numbers.append(parse(i+k[0], j+k[1]))
            ans1 += sum(numbers)
            if len(numbers) == 2 and lines[i][j] == '*':
                ans2 += numbers[0]*numbers[1]
print(ans1)
print(ans2)
