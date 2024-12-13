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
                                fencenow.append([t[0],t[1],m,0,'no'])
                        elif t[0]+m < 0:
                            fencenow.append([t[0],t[1],-1,0,'no'])
                        elif t[0]+m == len(data):
                            fencenow.append([t[0],t[1],1,0,'no'])
                        if 0 <= t[1]+m < len(data[0]):
                            if data[t[0]][t[1]+m] == letter and [t[0],t[1]+m] not in gothere:
                                gothere.append([t[0],t[1]+m])
                                area += 1
                                done = False
                            elif [t[0],t[1]+m] not in there and [t[0],t[1]+m] not in beenthere and [t[0],t[1]+m] not in gothere:
                                fencenow.append([t[0],t[1],0,m,'no'])
                        elif t[1]+m < 0:
                            fencenow.append([t[0],t[1],0,-1,'no'])
                        elif t[1]+m == len(data[0]):
                            fencenow.append([t[0],t[1],0,1,'no'])
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
            f0 = fencenow
            f = sorted(f0, key=lambda x: (x[0], x[1]))
            for n in range(len(f)):
                f[n][4] = 'yes'
                if [f[n][0]+f[n][3],f[n][1]+f[n][2],f[n][2],f[n][3],'yes'] not in f:
                    if [f[n][0]-f[n][3],f[n][1]-f[n][2],f[n][2],f[n][3],'yes'] not in f:
                        fence += 1
            #             print(f[n])
            # print(fence)
            # print(f)
            # input('ok')
            score += area*fence

print(score)
                
                        
#929608 is too high
#877626 is too high
#1046470
#877626
#877492 is correct

                
            
                        