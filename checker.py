data = [[1,6061]]

for k in range(len(data)):
    if len(str(data[k][1])) % 2 == 0:
       print(data[k])
       tosplit = str(data[k][1])
       halflen = int(len(tosplit)/2)
       print(tosplit,halflen)
       print(tosplit[halflen:],tosplit[:halflen])
       print([data[k][0],tosplit[halflen:]])
       print('here')
       # print(data[])
       data.insert(k+1,[data[k][0],tosplit[halflen:]])
       data[k][1] = tosplit[:halflen]
       print(data[k])
       print(data[k+1])
       input('ok')