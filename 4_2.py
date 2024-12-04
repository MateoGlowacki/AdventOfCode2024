import re
import numpy as np

data = open("../4_input.txt", 'r').readlines()

total = 0

for k in range(len(data)):
    for l in range(len(data[k])):
        if k != 0 and k != len(data)-1 and l != 0 and l != len(data[k])-1:
            if data[k][l] == 'A':
                if (data[k-1][l-1] == 'M' and data[k+1][l+1] == 'S') or (data[k-1][l-1] == 'S' and data[k+1][l+1] == 'M'):
                    if (data[k-1][l+1] == 'M' and data[k+1][l-1] == 'S') or (data[k-1][l+1] == 'S' and data[k+1][l-1] == 'M'):                 
                        total += 1

print(total)