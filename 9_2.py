data = open("../9_input.txt", 'r').readlines()[0].strip('\n')

entire = []

for k in range(len(data)):
    if k % 2 == 0:
        ID = int(k/2)
    else:
        ID = '.'
    if int(data[k]) != 0:
        entire.append([ID,int(data[k])])
        
# print(entire[10:])
# input('ok')

# entire = [[0,2],['.',3],[1,3],['.',3],[2,1],['.',3],[3,3],['.',1],[4,2],['.',1],[5,4],['.',1],[6,4],['.',1],[7,3],['.',1],[8,4],[9,2]]

checker = ['no']*10000

start = len(entire)
run1 = True
done = False
count = None

while done == False:
    
    if run1 == False:
        start = count
    run1 = False
    done = True
    count = 0
    
    for l in range(start-1,-1,-1):
        l += count
        if entire[l][0] != '.' and checker[entire[l][0]] == 'no':
            for k in range(l):
                if entire[k][0] == '.' and entire[k][1] >= entire[l][1]:
                    # print(k,l)
                    # print(count)
                    checker[entire[l][0]] = 'yes'
                    extra_length = entire[k][1] - entire[l][1]
                    entire[k] = entire[l].copy()
                    entire[l][0] = '.'
                    entire.insert(k+1,['.',extra_length])
                    count += 1
                    done = False
                    break

print('ok')

entire2 = []
for en in entire:
    entire2.extend([en[0]]*en[1])
    
print('ok2')

total = 0
for k in range(len(entire2)):
    if entire2[k] != '.':
        total += k*int(entire2[k])
    
print(total)

#30031033685 is too low
#15811986630969 is wrong
#12068578686220 is wrong
#12109244452608 is wrong
#13319119496818 is wrong
#13319119496818 is wrong