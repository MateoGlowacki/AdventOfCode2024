import re

data00 = open("../3_input.txt", 'r').readlines()

total = 0
count1 = 1

multi = r"mul\((\d+),(\d+)\)"

for data0 in data00:
    data = re.split("don't()", data0)
    
    for line0 in data:
        
        if count1 == 2:
            line1 = line0.split('do()')
            count2 = 0
            for line in line1:
                if count2 == 1:
                    results = re.findall(multi, line)
                    for result in results:
                        print(result)
                        total = total + int(result[0])*int(result[1])
                elif count2 == 0:
                    count2 = 1
        
        if count1 == 1:
            results = re.findall(multi, line0)
            for result in results:
                print(result)
                total = total + int(result[0])*int(result[1])
            count1 = 2
            
    
print(total)
