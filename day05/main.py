with open("input") as file:
    seedline = file.readline()
    file.readline()
    input = file.read()
input += '\n'

data = []
seedranges = []
seeds = [int(i) for i in seedline.strip('\n').split(":")[1].split()]
for i in range(len(seeds)//2):
    seedranges.append([int(seeds[2*i]), int(seeds[2*i+1])])
ranges = []
for i in input.splitlines():
    if i.find(":") == -1:
        if i == '':
            data.append(ranges)
            ranges = []
        else:
            ranges.append([int(i) for i in i.split()])

for ranges in data:
    newseeds = []
    newseedranges = []
    for subset in ranges:
        left = subset[1]
        right = subset[2]+left
        shift = subset[0] - subset[1]
        for i in range(len(seeds)):
            if left <= seeds[i] < right:
                newseeds.append(seeds[i] + shift)
        for i in range(len(seedranges)):
            seedleft = seedranges[i][0]
            seedright = seedleft+seedranges[i][1]
            if left < seedleft and seedleft < right and seedright > right:
                newseedranges.append([seedleft+shift, right-seedleft])
            elif left > seedleft and left < seedright and right > seedright:
                newseedranges.append([left+shift, seedright-left])
            elif seedleft <= left and seedright >= right:
                newseedranges.append([left+shift, right-left])
            elif left <= seedleft and right >= seedright:
                newseedranges.append([seedleft+shift, seedright-seedleft])
    seeds = newseeds
    seedranges = newseedranges


print(min(seeds))
print(min([i[0] for i in seedranges]))
