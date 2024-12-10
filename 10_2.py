data0 = open("../10_input.txt", 'r').readlines()

data = []

for line in data0:
    data.append(line.strip('\n'))

total = 0

for k in range(len(data)):
    for l in range(len(data[0])):
        num_now = 0
        if int(data[k][l]) == num_now:
            trail = [[k,l]]
            trailnow = 'ok'
            for num_now in range(1,10):
                
                if trailnow == []:
                    break
                trailnow = []
                
                for m in trail:
                    if m[0] > 0:
                        if int(data[m[0]-1][m[1]]) == num_now:
                            trailnow.append([m[0]-1,m[1]])
                    if m[0] < len(data)-1:
                        if int(data[m[0]+1][m[1]]) == num_now:
                            trailnow.append([m[0]+1,m[1]])
                    if m[1] > 0:
                        if int(data[m[0]][m[1]-1]) == num_now:
                            trailnow.append([m[0],m[1]-1])
                    if m[1] < len(data)-1:
                        if int(data[m[0]][m[1]+1]) == num_now:
                            trailnow.append([m[0],m[1]+1])
                trail = trailnow.copy()
                
                if num_now == 9:
                    total += len(trail)

print(total)
            
            