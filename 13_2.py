import re
import numpy as np

data0 = open("../13_input.txt", 'r').readlines()

score = 0

for i in range(int((len(data0)+1)/4)):
    textA = r"[+](\d+)"
    textB = r"[+](\d+)"
    textP = r"[=](\d+)"
    A = list(map(int, re.findall(textA, data0[4*i])))
    B = list(map(int, re.findall(textB, data0[4*i+1])))
    P = list(map(int, re.findall(textP, data0[4*i+2])))
    
    a = np.array([[A[0],B[0]],[A[1],B[1]]])
    b = np.array([P[0], P[1]])
    b = np.array([P[0]+10000000000000, P[1]+10000000000000])
    
    x = np.linalg.solve(a,b)
    
    if abs(x[0] - round(x[0])) < 0.001 and abs(x[1] - round(x[1])) < 0.001:
        score += 3*round(x[0]) + 1*round(x[1])

print(score)