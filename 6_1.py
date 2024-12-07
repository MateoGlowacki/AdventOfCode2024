data0 = open("../6_input.txt", 'r').readlines()

data = []
for line in data0:
    data.append(line.strip('\n'))
# print(data)

# def find_guard(layout):
#     for k in range(len(layout)):
#         for l in range(len(layout[k])):
#             if data[k][l] != '.' and data[k][l] != '#':
#                 position = [k,l]
#                 direction = data[k][l]
#     return(position, direction)

#16640 is too high
          
def count_path(layout):
    for k in range(len(layout)):
        for l in range(len(layout[k])):
            if data[k][l] != '.' and data[k][l] != '#':
                p0 = k
                p1 = l
                direction = data[k][l]
    
    
    if direction == '^':
        v0 = -1
        v1 = 0
    elif direction == '>':
        v0 = 0
        v1 = 1
    elif direction == 'v':
        v0 = 1
        v1 = 0
    elif direction == '<':
        v0 = 0
        v1 = -1
    
    layout[p0] = layout[p0][:p1] + 'X' + layout[p0][p1+1:]
    count = 1
    
    in_map = True
    while in_map == True:
        if p0+v0 == -1 or p0+v0 == len(layout) or p1+v1 == -1 or p1+v1 == len(layout[0]):
            in_map = False
        else:
            if layout[p0+v0][p1+v1] == '#':
                if v0 == -1:
                    v0 = 0
                    v1 = 1
                elif v1 == 1:
                    v0 = 1
                    v1 = 0
                elif v0 == 1:
                    v0 = 0
                    v1 = -1
                elif v1 == -1:
                    v0 = -1
                    v1 = 0
            elif layout[p0+v0][p1+v1] == '.':
                layout[p0] = layout[p0][:p1] + 'X' + layout[p0][p1+1:]
                p0 += v0
                p1 += v1
                count += 1
            elif layout[p0+v0][p1+v1] == 'X':
                layout[p0] = layout[p0][:p1] + 'X' + layout[p0][p1+1:]
                p0 += v0
                p1 += v1
                       
    return(count)

print(count_path(data))
            
        
            
        
        
    
    


