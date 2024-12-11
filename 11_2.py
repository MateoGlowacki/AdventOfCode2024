data0 = open("../11_input.txt", 'r').readlines()[0].strip("\n").split()

data = []

for line in data0:
    data.append([1,int(line)])
    
for blink in range(75):
    # print(data)
    print(blink)
    print(len(data))
    
    for k in range(len(data)-1,-1,-1):
        for l in range(k-1,-1,-1):
            if data[k][1] == data[l][1]:
                data[l][0] = data[k][0] + data[l][0]
                del data[k]
                break    
    
    count = 0
    for k in range(len(data)):
        k += count
        if data[k][1] == 0:
            data[k][1] = 1
        elif data[k][1] == 1:
            data[k][1] = 2024
        elif len(str(data[k][1])) % 2 == 0:
            tosplit = str(data[k][1])
            halflen = int(len(tosplit)/2)
            data.insert(k+1,[data[k][0],int(tosplit[halflen:])])
            data[k][1] = int(tosplit[:halflen])
            k += 1
            count += 1
        else:
            data[k][1] = data[k][1] * 2024

total = 0

for n in data:
    total += n[0]

print(total)