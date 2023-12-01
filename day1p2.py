# Day 1  AOC 2k23
with open('inputd1p1.txt','r')as file:
        file_content=file.read()
        inputval=(file_content).splitlines() #splits to list


# Eg val inp
example= ["two1nine","eightwothree"]
def day1func(example):
    sum=0
    digits=[ "one", "two", "three", "four", "five", "six", "seven", "eight","nine"]
    for x in example: 
        print(str(x))
        j=str(x)
        for x in 
        print(j.split(digits[x],1)[1])
        
        """ numlist = list(''.join(filter(str.isdigit, x)))
        num=(numlist[0])+(numlist[len(numlist)-1])
        sum=sum+int(num)
        #print(num1) """
    return sum

print(day1func(example))
            
        