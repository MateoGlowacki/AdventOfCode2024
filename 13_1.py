import re

data0 = open("../13_input.txt", 'r').readlines()

score = 0

for i in range(int((len(data0)+1)/4)):
    textA = r"[+](\d+)"
    textB = r"[+](\d+)"
    textP = r"[=](\d+)"
    A = list(map(int, re.findall(textA, data0[4*i])))
    B = list(map(int, re.findall(textB, data0[4*i+1])))
    P = list(map(int, re.findall(textP, data0[4*i+2])))
    
    cost = 999
    
    for j in range(101):
        for k in range (101):
            if j*A[0] + k*B[0] == P[0] and j*A[1] + k*B[1] == P[1]:
                costnow = 3*j + k
                if costnow < cost:
                    cost = costnow
    if cost != 999:
        # print(cost)
        # input('ok')
        score += cost

print(score)
