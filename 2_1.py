import numpy as np

data0 = open("../2_input.txt", 'r').readlines()

total = 0

for line0 in data0:
    # print(total)
    line = list(map(int, line0.split()))
    safe = True
    order = 0
    # print(line)
    
    for n in range(len(line)-1):
        # print(line[n])
        
        if line[n] == line[n+1]:
            safe = False
            break
        if line[n] < line[n+1]:
            if order == 2 or line[n+1]-line[n]>3:
                safe = False
                break
            order = 1
        if line[n] > line[n+1]:
            if order == 1 or line[n]-line[n+1]>3:
                safe = False
                break
            order = 2
            
    if safe == True:
        total = total+1
         
print(total)