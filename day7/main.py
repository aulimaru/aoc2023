map2 = {'J': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'Q': 10, 'K': 11, 'A': 12}
map1 = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}

with open("input") as file:
    input = file.read()

data = []


def hashs(s, map):
    r = 0
    for i in s:
        r *= 13
        r += map[i]
    return r


def solve(s, o, map):
    ty = ""
    nums = []
    for i in s:
        if i in ty:
            nums[ty.find(i)] += 1
        else:
            nums.append(1)
            ty += i
    return (len(ty)*10 - max(nums))*13**5-hashs(o, map)


for i in input.splitlines():
    data.append(i.split())


def solve2(s, map):
    r = []
    for i in map2.keys():
        r.append(solve(s.replace('J', i), s, map))
    return min(r)


def key2(a):
    return solve2(a[0], map2)


def key1(a):
    return solve(a[0], a[0], map1)


data.sort(key=key1, reverse=True)
ans1 = 0
for i in range(len(data)):
    ans1 += (i+1)*int(data[i][1])
data.sort(key=key2, reverse=True)
ans2 = 0
for i in range(len(data)):
    ans2 += (i+1)*int(data[i][1])
print(ans1)
print(ans2)
