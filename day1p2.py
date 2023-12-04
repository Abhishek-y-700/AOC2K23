# Day 1 p2  AOC 2k23
import re
with open('inputd1p1.txt','r')as file:
        file_content=file.read()
        inputval=(file_content).splitlines() #splits to list
#print(inputval)
var_digit = { "one":1 , "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8,"nine":9 }
# Eg val inp
example= ['sdpgz3five4seven6fiveh', '876mbxbrntsfm', 'fivek5mfzrdxfbn66nine8eight']
def day1func(example):
    sum=0
    for char in example:
        
        numlist = re.findall(r'(\d|one|two|three|four|five|six|seven|eight|nine)', char)
        print(numlist)
        print([var_digit.get(i, i) for i in numlist])
        tuple=[var_digit.get(i, i) for i in numlist]
        
        sum_tuple= int(tuple[0])*10 +int(tuple[len(tuple)-1])
        print(sum_tuple)
        sum= sum+ sum_tuple
        print(sum  ) 
        print('End func')
    return sum
    

print(day1func(inputval))
            
        