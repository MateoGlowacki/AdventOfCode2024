import re
import numpy as np

data = open("../4_input.txt", 'r').readlines()

def xmas(line):
    results1 = len(re.findall("XMAS", line))
    results2 = len(re.findall("SAMX", line))
    return(results1 + results2)

total = 0

data1 = [""] * len(data[0])
data2 = [""] * (len(data) + len(data[0]) - 1)
data3 = [""] * (len(data) + len(data[0]) - 1)

for k in range(len(data)):
    total += xmas(data[k])
    
    for l in range(len(data[k])):
        data1[l] += data[k][l]

        data2[k + l] += data[k][l]
        data3[k + len(data[k]) - 1 - l] += data[k][l]
            
        
for m in range(len(data1)):    
    total += xmas(data1[m])
    
for n in range(len(data2)):
    total += xmas(data2[n])
    
for o in range(len(data3)):
    total += xmas(data3[o])

print(total)