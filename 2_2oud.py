import numpy as np

data0 = open("../2_input.txt", 'r').readlines()

total = 0

for line0 in data0:
    # print(total)
    line = list(map(int, line0.split()))
    safe = True
    leeway = False
    safe0 = True
    order = 0
    
    # print(line)
    for n in range(len(line)-1):
        if line[n] == line[n+1]:
            leeway = True
            break
        if line[n] < line[n+1]:
            if order == 2 or line[n+1]-line[n]>3:
                leeway = True
                break
            else:
                order = 1
        if line[n] > line[n+1]:
            if order == 1 or line[n]-line[n+1]>3:
                leeway = True
                break
            else:
                order = 2
    
    if leeway == True:
        
        if n == 0:
            print('ok1')
            print(line)
            line2 = line.copy()
            del line2[1]
            print(line2)
            order = 0
            for n in range(len(line2)-1):
                if line2[n] == line2[n+1]:
                    safe0 = False
                    break
                if line2[n] < line2[n+1]:
                    if order == 2 or line2[n+1]-line2[n]>3:
                        safe0 = False
                        break
                    else:
                        order = 1
                if line2[n] > line2[n+1]:
                    if order == 1 or line2[n]-line2[n+1]>3:
                        safe0 = False
                        break
                    else:
                        order = 2
            if safe0 == False:
                del line[0]
                print('ok2')
                print(line)
                order = 0
                for n in range(len(line)-1):
                    if line[n] == line[n+1]:
                        safe = False
                        break
                    if line[n] < line[n+1]:
                        if order == 2 or line[n+1]-line[n]>3:
                            safe = False
                            break
                        else:
                            order = 1
                    if line[n] > line[n+1]:
                        if order == 1 or line[n]-line[n+1]>3:
                            safe = False
                            break
                        else:
                            order = 2      
            print(safe)
            input('oka')
                
        else:    
            # print(line)
            del line[n+1]
            # print(line)
            order = 0
            for n in range(len(line)-1):
                if line[n] == line[n+1]:
                    safe = False
                    break
                if line[n] < line[n+1]:
                    if order == 2 or line[n+1]-line[n]>3:
                        safe = False
                        break
                    else:
                        order = 1
                if line[n] > line[n+1]:
                    if order == 1 or line[n]-line[n+1]>3:
                        safe = False
                        break
                    else:
                        order = 2
            # print(safe)
            # input('okb')
                
            
    if safe == True:
        total = total+1
        
print(total)