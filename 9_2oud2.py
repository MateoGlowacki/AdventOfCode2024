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
while done == False:
    done = True
    if count == 0:
        start = 0
    else:
        start = len(entire)+count
        
    for k in range(start,len(entire)):
        if entire[k][0] == '.':
            for l in range(len(entire)-1,k,-1):
                if entire[l][0] != '.':
                    if entire[l][1]*len(str(entire[l][0])) == entire[k][1]*len(str(entire[k][0])):
                        entire[k] = entire[l].copy()
                        entire[l][0] = '.'
                        done = False
                        break
                    
                    elif entire[l][1]*len(str(entire[l][0])) < entire[k][1]*len(str(entire[k][0])):    
                        extra_length = entire[k][1]*len(str(entire[k][0])) - entire[l][1]*len(str(entire[l][0]))
                        entire[k] = entire[l].copy()
                        entire.insert(k+1,['.',extra_length])
                        entire[l+1][0] = '.'
                        count += 1
                        done = False
                        break


entire2 = []
for en in entire:
    entire2.extend([en[0]]*en[1])
    
total = 0
for k in range(len(entire2)):
    if entire2[k] != '.':
        total += k*int(entire2[k])
    
print(total)