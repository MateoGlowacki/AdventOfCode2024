data0 = open("../15_input.txt", 'r').readlines()

split = data0.index('\n')
warehouse0 = data0[:split]
moves0 = data0[split+1:]

wh = []
for ware0 in warehouse0:
    warenow = ''
    # print(ware0)
    for wa0 in ware0:
        if wa0 == '#':
            wa = '##'
        elif wa0 == 'O':
            wa = '[]'
        elif wa0 == '.':
            wa = '..'
        elif wa0 == '@':
            wa = '@.'
        elif wa0 == '\n':
            break
        warenow += wa    
    wh.append(warenow)

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

n=0

for move in moves:
        
    n += 1
    
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
    elif wh[ry+dy][rx+dx] == '[' or wh[ry+dy][rx+dx] == ']':
        
        if dx != 0:
            for i in range(2,199):
                if wh[ry][rx+i*dx] == '#':
                    break
                elif wh[ry][rx+i*dx] == '[' or wh[ry][rx+i*dx] == ']':
                    lmao = True
                elif wh[ry][rx+i*dx] == '.':
                    wh[ry] = wh[ry][:rx] + '.' + wh[ry][rx+1:]
                    for j in range(2,i+1):
                        if dx == 1:
                            a = '['
                            b = ']'
                        elif dx == -1:
                            a = ']'
                            b = '['
                        if j % 2 == 0:
                            wh[ry] = wh[ry][:rx+j*dx] + a + wh[ry][rx+j*dx+1:]
                        else: 
                            wh[ry] = wh[ry][:rx+j*dx] + b + wh[ry][rx+j*dx+1:]
                    rx += dx
                    wh[ry] = wh[ry][:rx] + '@' + wh[ry][rx+1:]
                    break
        
        elif dy != 0:
            boxold = []
            boxnow = []
            boxnew = []
            boxnewnow = []
            if wh[ry+dy][rx] == '[':
                boxnow.append([ry+dy,rx,'['])
                boxnow.append([ry+dy,rx+1,']'])
            elif wh[ry+dy][rx] == ']':
                boxnow.append([ry+dy,rx,']'])
                boxnow.append([ry+dy,rx-1,'['])
            done = False            
            
            while done == False:
                done = True
                free = True
                boxnewnow = []
                for b in boxnow:
                    boxnewnow.append([b[0]+dy,b[1],b[2]])
                boxold.extend(boxnow)
                boxnow = []
                for c in boxnewnow:
                    if wh[c[0]][c[1]] == '#':
                        done = True
                        free = False
                        break
                    elif wh[c[0]][c[1]] == '[':
                        if [c[0],c[1],'['] not in boxnow:
                            done = False
                            boxnow.append([c[0],c[1],'['])
                            boxnow.append([c[0],c[1]+1,']'])
                    elif wh[c[0]][c[1]] == ']':
                        if [c[0],c[1],']'] not in boxnow:
                            done = False
                            boxnow.append([c[0],c[1],']'])
                            boxnow.append([c[0],c[1]-1,'['])
                boxnew.extend(boxnewnow)
        
            if free == True:
                for b in boxold:
                    wh[b[0]] = wh[b[0]][:b[1]] + '.' + wh[b[0]][b[1]+1:]
                for b in boxnew:
                    wh[b[0]] = wh[b[0]][:b[1]] + b[2] + wh[b[0]][b[1]+1:]
                wh[ry] = wh[ry][:rx] + '.' + wh[ry][rx+1:]
                ry += dy
                wh[ry] = wh[ry][:rx] + '@' + wh[ry][rx+1:]
                
GPS = 0
for i in range(len(wh)):
    for j in range(len(wh[0])):
        if wh[i][j] == '[':
            GPS += i*100 + j

print(GPS)