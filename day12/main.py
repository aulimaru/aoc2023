#with open("input") as file:
with open("test") as file:
    input = file.read()

data = []
maps = []
for i in input.splitlines():
    i = i.strip('\n').split()
    maps.append(i[0])
    d = [int(i) for i in i[1].split(',')]
    data.append(d)


def 
