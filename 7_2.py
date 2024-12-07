# import numpy as np
# data = np.loadtxt("../7_input.txt", dtype=int)
data = open("../7_input.txt", 'r').readlines()

print(data)

total = 0

for line in data:
    line = line.replace(':','').split()
    
    results = [int(line[1])]
    
    for n in range(2,len(line)):
        resultsnow = []
        for result in results:
            resultsnow.append(result+int(line[n]))
            resultsnow.append(result*int(line[n]))
            resultsnow.append(int(str(result)+line[n]))
        results = resultsnow
    
    for result in results:
        if result == int(line[0]):
            total += result
            break
            
print(total)