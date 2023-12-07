words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def parse(line):
    index = 65536
    value = 0
    result1 = 0
    result2 = 0
    for i in range(1, 10):
        pos = line.find(str(i))
        if pos < index and pos != -1:
            index = pos
            value = i
    result1 += value
    for i in range(1, 10):
        pos = line.find(words[i-1])
        if pos < index and pos != -1:
            index = pos
            value = i
    result2 += value
    result1 *= 10
    result2 *= 10
    index = -1
    value = 0
    for i in range(1, 10):
        pos = line.rfind(str(i))
        if pos > index and pos != -1:
            index = pos
            value = i
    result1 += value
    for i in range(1, 10):
        pos = line.rfind(words[i-1])
        if pos > index and pos != -1:
            index = pos
            value = i
    result2 += value
    return result1, result2


with open("input") as file:
    input = file.read()

ans1 = 0
ans2 = 0
for i in input.splitlines():
    result = parse(i.strip())
    ans1 += result[0]
    ans2 += result[1]
print(ans1)
print(ans2)
