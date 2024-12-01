import numpy as np

data = np.loadtxt("../1_input.txt", dtype=int)
column1a = data[:,0]
column1b = column1a[column1a.argsort()]
column2a = data[:,1]
column2b = column2a[column2a.argsort()]

total = 0


for i in range(len(column1a)):
    # print(i)
    dist = abs(column1b[i]-column2b[i])
    # print(dist)
    total = total+dist
     
    
    # print(total)
    
print(total)

