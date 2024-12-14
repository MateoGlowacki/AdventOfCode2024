import regex as re

data0 = open("../14_input.txt", 'r').readlines()

robots = []

for line in data0:
    rob = list(map(int,re.findall(r'[-\d]+', line)))
    robots.append(rob)

Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0

for rob in robots:
    row = (rob[1]+rob[3]*100) % 103
    col = (rob[0]+rob[2]*100) % 101
    if row < 51:
        if col < 50:
            Q1 += 1
        elif col > 50:
            Q2 += 1
    elif row > 51:
        if col < 50:
            Q3 += 1
        elif col > 50:
            Q4 += 1

sf = Q1 * Q2 * Q3 * Q4

print(sf)     