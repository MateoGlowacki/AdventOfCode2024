import regex as re

data0 = open("../14_input.txt", 'r').readlines()

robots = []

for line in data0:
    rob = list(map(int,re.findall(r'[-\d]+', line)))
    robots.append(rob)

time = 0
done = False

while done == False:
    if time > 9999:
        print('failure')
        break
    if time % 100 == 0:
        print(time)
    robotsnew = []
    for i in range(len(robots)):
        colnow = robots[i][0]
        rownow = robots[i][1]
        if any(rob2[0] == colnow-1 and rob2[1] == rownow+1 for rob2 in robots):
            if any(rob2[0] == colnow+1 and rob2[1] == rownow+1 for rob2 in robots):
                b1 = any(rob2[0] == colnow-2 and rob2[1] == rownow+2 for rob2 in robots)
                b2 = any(rob2[0] == colnow-1 and rob2[1] == rownow+2 for rob2 in robots)
                b3 = any(rob2[0] == colnow+1 and rob2[1] == rownow+2 for rob2 in robots)
                b4 = any(rob2[0] == colnow+2 and rob2[1] == rownow+2 for rob2 in robots)
                c1 = any(rob2[0] == colnow and rob2[1] == rownow+3 for rob2 in robots)
                if b1 and b2 and b3 and b4 and c1:
                    done = True
                    print('done')
                    break
        col = (robots[i][0]+robots[i][2]) % 101
        row = (robots[i][1]+robots[i][3]) % 103
        robotsnew.append([col,row,robots[i][2],robots[i][3]])
    robots = robotsnew.copy()
    if done == False:
        time += 1

print(time)     