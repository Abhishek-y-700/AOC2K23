# Day 1  AOC 2k23
with open('inputd1p1.txt','r')as file:
        file_content=file.read()
        inputval=list(file_content)

# Eg val inp
example= ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]
def day1func(example):
    for x in example: 
        #print("testing")
        num1 = (''.join(filter(str.isdigit, x)))
        print(num1)

day1func(example)
            
        