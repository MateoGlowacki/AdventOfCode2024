data0 = open("../12_input.txt", 'r').readlines()

data = []

for line in data0:
    data.append(line.strip('\n'))

score = 0

for k in range(len(data)):
    for l in range(len(data[0])):
        if data[k][l] != '.':
            letter = data[k][l]
            beenthere = []
            there = [[k,l]]
            gothere = []
            done = False
            area = 1
            fence = 0
            fencenow = []
            while done == False:
                done = True
                for t in there:
                    for m in range(-1,2,2):
                        if 0 <= t[0]+m < len(data):
                            if data[t[0]+m][t[1]] == letter and [t[0]+m,t[1]] not in gothere:
                                gothere.append([t[0]+m,t[1]])
                                area += 1
                                done = False
                            elif [t[0]+m,t[1]] not in there and [t[0]+m,t[1]] not in beenthere and [t[0]+m,t[1]] not in gothere:
                                fencenow.append([t[0],t[1],m,0])
                                if [t[0],t[1]-1,m,0] not in fencenow and [t[0],t[1]+1,m,0] not in fencenow:
                                    fence += 1
                        elif t[0]+m < 0:
                            fencenow.append([t[0],t[1],-1,0])
                            if [t[0],t[1]-1,-1,0] not in fencenow and [t[0],t[1]+1,-1,0] not in fencenow:
                                fence += 1
                        elif t[0]+m == len(data):
                            fencenow.append([t[0],t[1],1,0])
                            if [t[0],t[1]-1,1,0] not in fencenow and [t[0],t[1]+1,1,0] not in fencenow:
                                fence += 1
                        if 0 <= t[1]+m < len(data[0]):
                            if data[t[0]][t[1]+m] == letter and [t[0],t[1]+m] not in gothere:
                                gothere.append([t[0],t[1]+m])
                                area += 1
                                done = False
                            elif [t[0],t[1]+m] not in there and [t[0],t[1]+m] not in beenthere and [t[0],t[1]+m] not in gothere:
                                fencenow.append([t[0],t[1],0,m])
                                if [t[0]-1,t[1],0,m] not in fencenow and [t[0]+1,t[1],0,m] not in fencenow:
                                    fence += 1
                        elif t[1]+m < 0:
                            fencenow.append([t[0],t[1],0,-1])
                            if [t[0]-1,t[1],0,-1] not in fencenow and [t[0]+1,t[1],0,-1] not in fencenow:
                                fence += 1
                        elif t[1]+m == len(data[0]):
                            fencenow.append([t[0],t[1],0,1])
                            if [t[0]-1,t[1],0,1] not in fencenow and [t[0]+1,t[1],0,1] not in fencenow:
                                fence += 1
                    data[t[0]] = data[t[0]][:t[1]] + '.' + data[t[0]][t[1]+1:]
                    beenthere.append(t)
                there = gothere
                gothere = []
                # print(data[:10])
                # print(beenthere)
                # print(there)
                # print(gothere)
                # print(area)
                # print(fence)
                # input('ok')
            score += area*fence

print(score)
                
                        
#929608 is too high
#877626 is too high

                
            
                        