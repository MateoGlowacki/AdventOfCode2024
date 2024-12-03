data = open("../3_input.txt", 'r').readlines()

total = 0


for line in data:
    mul = False
    number = 0
    num1 = None
    num2 = None
    for i in range(len(line)):
        if mul == True:
            if number == 2:
                
                if line[i] == ')' and num2 is not None:
                    total = total + (int(num1)*int(num2))
                    mul = False
                    number = 0
                    num1 = None
                    num2 = None
                    
                elif line[i].isnumeric():
                    if num2 is not None:
                        num2 = num2 + line[i]
                    else:
                        num2 = line[i]
                        
                else:
                    mul = False
                    number = 0
                    num1 = None
                    num2 = None
                    
            if number == 1:
                
                if line[i].isnumeric():
                    if num1 is not None:
                        num1 = num1 + line[i]
                    else:
                        num1 = line[i]
                        
                elif line[i] == ',' and num1 is not None:
                    number = 2
                    
                else:
                    mul = False
                    number = 0
                    num1 = None   
                    
            if line[i-1] == '(':
                number = 1
       
        if line[i] == 'm':
            if line[i+1] == 'u' and line[i+2] == 'l' and line[i+3] == '(':
                mul = True
        
                
print(total)