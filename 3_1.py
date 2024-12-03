import re

data = open("../3_input.txt", 'r').readlines()

total = 0

multi = r"mul\((\d+),(\d+)\)"

for line in data:
    results = re.findall(multi, line)
    for result in results:
        total = total + int(result[0])*int(result[1])
                
print(total)