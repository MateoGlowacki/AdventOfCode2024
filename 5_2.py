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

lines2 = []
for line in lines:
    correct = True
    for n in range(len(line)):
        for rule in rules:
            if line[n] == rule[1]:
                for m in range(n, len(line)):
                    if line[m] == rule[0]:
                        correct = False 
    if correct == False:
        lines2.append(line)

rules2 = []
for n in range(len(rules)):    
    if n != 0:            
        if rules[n][0] < rules2[0][0]:
            rules2.insert(0,rules[n])
        else:
            for m in range(len(rules2)):
                
                if rules[n][0] == rules2[m][0]:
                    if rules[n][1] < rules2[m][1]:
                        rules2.insert(m,rules[n])
                        break
                    elif m+1 == len(rules2):
                        rules2.append(rules[n])
                        break
                    elif rules[n][0] < rules2[m+1][0]:
                        rules2.insert(m+1,rules[n])
                        break
                    
                elif m+1 == len(rules2):
                    rules2.append(rules[n])
                    break
                    
                elif rules[n][0] > rules2[m-1][0] and rules[n][0] < rules2[m][0]:
                    rules2.insert(m,rules[n])
                    break
    elif n == 0:
        rules2.append(rules[0])

rules3=[rules2[0][0]]

busy = 1
while busy != 0:
    busy = 0
    for n in range(len(rules2)):
        left = None
        right = None
        for m in range(len(rules3)):
            if rules2[n][0] == rules3[m]:
                left = m
            elif rules2[n][1] == rules3[m]:
                right = m
        if left is None and right is None:
            busy +=0
        elif left is not None and right is None:
            rules3.insert(left+1,rules2[n][1])
            busy +=1
        elif left is None and right is not None:
            rules3.insert(right,rules2[n][0])
            busy +=1
        elif left > right:
            del rules3[left]
            rules3.insert(right,rules2[n][0])
            busy +=1
    print(busy)
    input('ok')
        

print(rules3)


