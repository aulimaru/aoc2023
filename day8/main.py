with open("input") as file:
    instructions = [int(i) for i in file.readline().strip('\n').replace('L', '0').replace('R', '1')]
    file.readline()
    input = file.read()
data = {}
for line in input.splitlines():
    line = line.split(' = ')
    dest = line[1].replace('(', '').replace(')', '').replace(',', '').split()
    data[line[0]] = dest


def findgcd(a, b):
    if b == 0:
        return a
    return findgcd(b, a % b)


def findlcm(numbers):
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        num = numbers[i]
        gcd = findgcd(lcm, num)
        lcm = (lcm * num) // gcd
    return lcm


def notfull(firstz):
    for i in firstz:
        if i is None:
            return True
    return False


step = 0
index = 0
current = "AAA"
while current != "ZZZ":
    current = data[current][instructions[index]]
    step += 1
    index = (index + 1) % len(instructions)
ans1 = step
step = 0
index = 0
currents = []
firstz = []
for i in data.keys():
    if i[2] == 'A':
        currents.append(i)
        firstz.append(None)
while notfull(firstz):
    for i in range(len(currents)):
        if currents[i][2] == 'Z':
            firstz[i] = step
    newcurrents = []
    for i in currents:
        newcurrents.append(data[i][instructions[index]])
    step += 1
    index += 1
    currents = newcurrents
    index = index % len(instructions)
ans2 = findlcm(firstz)
print(ans1)
print(ans2)
