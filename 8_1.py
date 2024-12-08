data0 = open("../8_input.txt", 'r').readlines()

data = []

for line in data0:
    data.append(line.strip('\n'))

# print(data)

height = len(data)-1
width = len(data[0])-1
antennas = []

for k in range(len(data)):
    for l in range(len(data[0])):
        if data[k][l] != '.':
            antennas.append([data[k][l],k,l])

locs = []

for antenna1 in antennas:
    for antenna2 in antennas:
        if antenna1[0] == antenna2[0] and antenna1 != antenna2:
            
            loc1 = 0
            loc2 = 0
            
            locok = True
            
            if antenna1[1] < antenna2[1]:
                loc1 = antenna1[1] - (antenna2[1] - antenna1[1])
            elif antenna1[1] > antenna2[1]:
                loc1 = antenna1[1] + (antenna1[1] - antenna2[1])
            if antenna1[2] < antenna2[2]:
                loc2 = antenna1[2] - (antenna2[2] - antenna1[2])
            elif antenna1[2] > antenna2[2]:
                loc2 = antenna1[2] + (antenna1[2] - antenna2[2])
            if 0 <= loc1 <= height and 0 <= loc2 <= width:
                for loc in locs:
                    if [loc1,loc2] == loc:
                        locok = False
                        break
                if locok == True:
                    locs.append([loc1,loc2])
                
            
print(len(locs))
            