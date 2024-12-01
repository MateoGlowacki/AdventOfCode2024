import numpy as np

data = np.loadtxt("../1_input.txt", dtype=int)
column1a = data[:,0]
# column1b = column1a[column1a.argsort()]
column2a = data[:,1]
# column2b = column2a[column2a.argsort()]

total = 0


for i in column1a:
    present = 0
    for j in column2a:
        if i == j:
            present = present+1

    total = total+present*i
     
    
    
print(total)

