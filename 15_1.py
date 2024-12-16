data0 = open("../15_input.txt", 'r').readlines()

split = data0.index('\n')
warehouse0 = data0[:split]
moves0 = data0[split+1:]

wh = []
for ware0 in warehouse0:
    wh.append(ware0.strip('\n'))

moves = ''
for move0 in moves0:
    move = move0.strip('\n')
    moves += move

found_robot = False
for i in range(len(wh)):
    for j in range(len(wh[0])):
        if wh[i][j] == '@':
            ry = i
            rx = j
            found_robot = True
            break
    if found_robot == True:
        break

for move in moves:
    dx = 0
    dy = 0
    if move == 'v':
        dy = 1
    elif move == '^':
        dy = -1
    elif move == '>':
        dx = 1
    elif move == '<':
        dx = -1
    if wh[ry+dy][rx+dx] == '#':
        lmao = True
    elif wh[ry+dy][rx+dx] == '.':
        wh[ry] = wh[ry][:rx] + '.' + wh[ry][rx+1:]
        ry += dy
        rx += dx
        wh[ry] = wh[ry][:rx] + '@' + wh[ry][rx+1:]
    elif wh[ry+dy][rx+dx] == 'O':
        for i in range(2,99):
            if wh[ry+i*dy][rx+i*dx] == '#':
                break
            elif wh[ry+i*dy][rx+i*dx] == 'O':
                lmao = True
            elif wh[ry+i*dy][rx+i*dx] == '.':
                wh[ry] = wh[ry][:rx] + '.' + wh[ry][rx+1:]
                wh[ry+i*dy] = wh[ry+i*dy][:rx+i*dx] + 'O' + wh[ry+i*dy][rx+i*dx+1:]
                ry += dy
                rx += dx
                wh[ry] = wh[ry][:rx] + '@' + wh[ry][rx+1:]
                break
    
GPS = 0
for i in range(len(wh)):
    for j in range(len(wh[0])):
        if wh[i][j] == 'O':
            GPS += 100*i + j

print(GPS)
    