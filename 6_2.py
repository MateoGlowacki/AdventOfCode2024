data0 = open("../6_input.txt", 'r').readlines()

layout0 = []
for line in data0:
    layout0.append(line.strip('\n'))
      
for k0 in range(len(layout0)):
    for l0 in range(len(layout0[k0])):
        if layout0[k0][l0] != '.' and layout0[k0][l0] != '#':
            k00 = k0
            l00 = l0
            direction0 = layout0[k0][l0]


if direction0 == '^':
    v00 = -1
    v10 = 0
elif direction0 == '>':
    v00 = 0
    v10 = 1
elif direction0 == 'v':
    v00 = 1
    v10 = 0
elif direction0 == '<':
    v00 = 0
    v10 = -1

loops = 0

for k in range(len(layout0)):
    # print(k)
    for l in range(len(layout0[k])):
        # print(l)
        if k == k00 and l == l00:
            print(k)
            print(k00)
            print(l)
            print(l00)
            # input('ok')
        else:
            p0 = k00
            p1 = l00
            v0 = v00
            v1 = v10
            direction = direction0
            layout = layout0.copy()
            layout[k] = layout[k][:l] + '#' + layout[k][l+1:]
            
            visited = []

            in_map = True
            count = 0
            while in_map == True:
                count += 1
                if count == 9999:
                    in_map = False
                    loops += 1
                if p0+v0 == -1 or p0+v0 == len(layout) or p1+v1 == -1 or p1+v1 == len(layout[0]):
                    in_map = False
                else:
                    if layout[p0+v0][p1+v1] == direction:
                        in_map = False
                        loops += 1
                    elif layout[p0+v0][p1+v1] == '#':
                        if v0 == -1:
                            v0 = 0
                            v1 = 1
                            direction = '>'
                        elif v1 == 1:
                            v0 = 1
                            v1 = 0
                            direction = 'v'
                        elif v0 == 1:
                            v0 = 0
                            v1 = -1
                            direction = '<'
                        elif v1 == -1:
                            v0 = -1
                            v1 = 0
                            direction = '^'
                    elif layout[p0+v0][p1+v1] != direction:
                        layout[p0] = layout[p0][:p1] + direction + layout[p0][p1+1:]
                        p0 += v0
                        p1 += v1
                        # visit = [p0,p1,direction]
                        # for check in visited:
                        #     if visit == check:
                        #         in_map = False
                        #         loops +=1
                        # visited.append(visit)

print(loops)

#1639 is too low
        
        
    
    


