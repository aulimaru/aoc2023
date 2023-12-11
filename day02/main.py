colors = ["red", "green", "blue"]
maxnumber = [12, 13, 14]


def parse(s):
    r = ""
    i = 0
    while '0' <= s[i] <= '9':
        r += s[i]
        i += 1
    return int(r)


with open("input") as file:
    input = file.read()
ans1 = 0
ans2 = 0
data = []
for i in input.splitlines():
    game = []
    for j in i.split(":")[1].split(";"):
        revealed = []
        for k in j.split(","):
            k = k.split()
            revealed.append([int(k[0]), k[1]])
        game.append(revealed)
    data.append(game)
for gamenumber in range(len(data)):
    multiplyer = 1
    possible = True
    for colornumber in range(len(colors)):
        minpossible = 0
        for revealed in data[gamenumber]:
            for balls in revealed:
                if balls[1] == colors[colornumber]:
                    if balls[0] > maxnumber[colornumber]:
                        possible = False
                    minpossible = max(minpossible, balls[0])
        multiplyer *= minpossible
    if possible:
        ans1 += gamenumber+1
    ans2 += multiplyer
print(ans1)
print(ans2)
