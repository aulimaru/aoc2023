with open("input") as file:
    input = file.read()
data = []
mult = []
for i in input.splitlines():
    i = i.split(':')[1].split('|')
    data.append([i[0].split(), i[1].split()])
    mult.append(0)
ans1 = 0
mult[0] = 1
for i in range(len(data)):
    card = data[i]
    match = 0
    for j in card[0]:
        if j in card[1]:
            match += 1
    if match > 0:
        ans1 += 2**(match-1)
    if i+1 < len(mult):
        mult[i+1] += mult[i]
        if i+match+1 < len(mult):
            mult[i+match+1] -= mult[i]
        mult[i+1] += mult[i]
print(ans1)
print(sum(mult))
