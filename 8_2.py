import math

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
            
            delta01 = antenna2[1] - antenna1[1]
            delta02 = antenna2[2] - antenna1[2]
            div = math.gcd(delta01, delta02)
            delta1 = int(delta01/div)
            delta2 = int(delta02/div)
            
            loc1 = antenna1[1]
            loc2 = antenna1[2]            
            
            while 0 <= loc1 <= height and 0 <= loc2 <= width:
                locok = True
                for loc in locs:
                    if [loc1,loc2] == loc:
                        locok = False
                        break
                if locok == True:
                    locs.append([loc1,loc2])
                loc1 += delta1
                loc2 += delta2
            
            loc1 = antenna1[1]
            loc2 = antenna1[2]
            
            while 0 <= loc1 <= height and 0 <= loc2 <= width:
                locok = True
                for loc in locs:
                    if [loc1,loc2] == loc:
                        locok = False
                        break
                if locok == True:
                    locs.append([loc1,loc2])   
                loc1 -= delta1
                loc2 -= delta2
                        
print(len(locs))
            