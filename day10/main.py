import sys
sys.setrecursionlimit(3000000)
with open("input") as file:
    input = file.read()
data = []
distance = []
for i in input.splitlines():
    data.append(list(i.strip('\n')))
    distance.append([None for i in i.strip('\n')])

startPoint = [0, 0]

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'S':
            startPoint = [i, j]

directions = {
    "w": [-1, 0],
    "a": [0, -1],
    "s": [1, 0],
    "d": [0, 1],
}


routes = {
    "F": {"w": "d", "a": "s"},
    "7": {"w": "a", "d": "s"},
    "L": {"a": "w", "s": "d"},
    "J": {"s": "a", "d": "w"},
    "|": {"w": "w", "s": "s"},
    "-": {"a": "a", "d": "d"},
}


match = {
    "F": "J",
    "L": "7",
}


def addPoints(a, b):
    return [a[0]+b[0], a[1]+b[1]]


def turn(route, direction):
    if route in routes:
        if direction in routes[route]:
            return routes[route][direction]
    return None


def inArea(point):
    if point[0] < 0 or point[0] >= len(data):
        return False
    if point[1] < 0 or point[1] >= len(data[point[0]]):
        return False
    return True


def search(point, direction, count):
    if not inArea(point):
        return None
    direction = turn(data[point[0]][point[1]], direction)
    if direction is None:
        return None
    if distance[point[0]][point[1]] is None:
        distance[point[0]][point[1]] = count
    else:
        distance[point[0]][point[1]] = min(count, distance[point[0]][point[1]])
    point = addPoints(point, directions[direction])
    search(point, direction, count+1)


connected = []
distance[startPoint[0]][startPoint[1]] = 0
for direction in directions:
    point = addPoints(startPoint, directions[direction])
    if inArea(point) and turn(data[point[0]][point[1]], direction) is not None:
        connected.append(direction)
        search(point, direction, 0)
connected.sort()
for route in routes:
    routeConnected = list(routes[route])
    routeConnected.sort()
    if connected == routeConnected:
        data[startPoint[0]][startPoint[1]] = route


ans1 = 0
ans2 = 0
for i in range(len(data)):
    include = False
    for j in range(len(data[i])):
        if distance[i][j] is None:
            if include:
                ans2 += 1
            continue
        ans1 = max(ans1, distance[i][j])
        route = data[i][j]
        if route in match:
            start = route
        elif route in match.values():
            if match[start] == route:
                include = not include
        if route == '|':
            include = not include


print(ans1)
print(ans2)
