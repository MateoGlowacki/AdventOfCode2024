import numpy as np

data = open("../5_input.txt", 'r').readlines()

split = data.index('\n')

rules0 = data[:split]
lines0 = data[split+1:]

rules = []
lines = []

for rule0 in rules0:
    n1 = int(rule0[0]+rule0[1])
    n2 = int(rule0[3]+rule0[4])
    rules.append([n1,n2])

for line0 in lines0:
    lines.append(np.fromstring(line0, dtype=int, sep=','))
    
total = 0

for line in lines:
    correct = True
    
    for n in range(len(line)):
        for rule in rules:
            if line[n] == rule[1]:
                for m in range(n, len(line)):
                    if line[m] == rule[0]:
                        correct = False
                     
    if correct == True:
        total += line[int((len(line)-1)/2)]
    
print(total)                                                
        
    
                        
                
        
                