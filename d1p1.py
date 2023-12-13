# Day 1  AOC 2k23
with open('inputd1p1.txt','r')as file:
        file_content=file.read()
        inputval=(file_content).splitlines()

print(inputval)
# Eg val inp
example= ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]
def day1func(example):
    sum=0
    for x in example: 
        #print("testing")
        numlist = list(''.join(filter(str.isdigit, x)))
        num=(numlist[0])+(numlist[len(numlist)-1])
        sum=sum+int(num)
        #print(num1)
    return sum

print(day1func(inputval))
            
        
