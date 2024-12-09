data = open("../9_input.txt", 'r').readlines()[0].strip('\n')

entire = []

for k in range(len(data)):
    if k % 2 == 0:
        ID = int(k/2)
    else:
        ID = '.'
    entire.extend(int(data[k])*[ID])

done = False
for k in range(len(entire)):
    if done == True:
        break
    elif entire[k] == '.':
        for l in range(len(entire)-1,-1,-1):
            if k == l:
                done = True
                break
            elif entire[l] != '.':
                entire[k] = entire[l]
                entire[l] = '.'
                break

total = 0

for k in range(len(entire)):
    if entire[k] == '.':
        break
    else:
        total += k*entire[k]
    
print(total)
