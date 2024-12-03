import numpy as np

def test(line):
    score = 1
    order = 0
    for n in range(len(line)-1):
        if line[n] == line[n+1]:
            score = 0
            break
        if line[n] < line[n+1]:
            if order == 2 or line[n+1]-line[n]>3:
                score = 0
                break
            order = 1
        if line[n] > line[n+1]:
            if order == 1 or line[n]-line[n+1]>3:
                score = 0
                break
            order = 2
    return(score,n)

data0 = open("../2_input.txt", 'r').readlines()

total = 0

for line0 in data0:
    countnow = 0
    linenow = list(map(int, line0.split()))
    
    result = test(linenow)
    
    if result[0] == 1:
        countnow = 1
    
    else:
        ident = result[1]
        
        if ident == 0:
            linenow1 = linenow.copy()
            del linenow[0]
            del linenow1[1]
            
            countnow = test(linenow)[0]
            
            if countnow == 0:
                countnow = test(linenow1)[0]
        
        else:
            linenow1 = linenow.copy()
            linenow2 = linenow.copy()
            del linenow[ident-1]
            del linenow1[ident]
            del linenow2[ident+1]
            
            countnow = test(linenow)[0]
            
            if countnow == 0:
                countnow = test(linenow1)[0]
                
                if countnow == 0:
                    countnow = test(linenow2)[0]

    total = total + countnow   
         
print(total)