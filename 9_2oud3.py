data = open("../9_input.txt", 'r').readlines()[0].strip('\n')

entire = []

for k in range(len(data)):
    if k % 2 == 0:
        ID = int(k/2)
    else:
        ID = '.'
    if int(data[k]) != 0:
        entire.append([ID,int(data[k])])

done = False
count = 0
start = len(entire)
loop1 = Truechecker = ['no']*10
checker = ['no']*10000

while done == False:
    print(entire[k-10:k+10])
    print(count)
    input('ok')
    done = True
    if loop1 == False:
        start = lastl
    loop1 = False
    count = 0
    
    for l in range(start-1,-1,-1):
        l += count
        for k in range(l):
            if entire[k][0] == '.':
                if entire[l][0] != '.' and checker[int(entire[l][0])] != 'yes':
                    if entire[l][1]*len(str(entire[l][0])) == entire[k][1]*len(str(entire[k][0])):
                        checker[int(entire[l][0])] = 'yes'
                        entire[k] = entire[l].copy()
                        entire[l][0] = '.'
                        done = False
                        break
                    
                    elif entire[l][1]*len(str(entire[l][0])) < entire[k][1]*len(str(entire[k][0])):  
                        checker[int(entire[l][0])] = 'yes'
                        extra_length = entire[k][1]*len(str(entire[k][0])) - entire[l][1]*len(str(entire[l][0]))
                        entire[k] = entire[l].copy()
                        entire.insert(k+1,['.',extra_length])
                        entire[l+1][0] = '.'
                        done = False
                        print('ok4')
                        print(k,l)
                        break
        lastl = l

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