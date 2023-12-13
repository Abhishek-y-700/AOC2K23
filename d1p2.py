# Day 1 p2  AOC 2k23
import re
with open('inputd1p1.txt','r')as file:
        file_content=file.read()
        inputval=(file_content).splitlines() #splits to list

#print(inputval)
var_digit = { "one":1 , "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8,"nine":9 }
# Eg val inp
example= ['sdpgz3five4seven6fiveh', '876mbxbrntsfm', 'fivek5mfzrdxfbn66nine8eight','a7a']
def day1func(example):
    sum=0
    for char in example:
        char_rep= re.sub('one', 'o1e', char, re.I)
        char_rep= re.sub('two', 't2o', char_rep, re.I)
        char_rep= re.sub('three', 't3e', char_rep, re.I)
        char_rep= re.sub('four', 'f4r', char_rep, re.I)
        char_rep= re.sub('five', 'f5e', char_rep, re.I)
        char_rep= re.sub('six', 's6x', char_rep, re.I)
        char_rep= re.sub('seven', 's7n', char_rep, re.I)
        char_rep= re.sub('eight', 'e8t', char_rep, re.I)
        char_rep= re.sub('nine', 'n9e', char_rep, re.I)

        numlist = re.findall(r'(\d|one|two|three|four|five|six|seven|eight|nine)', char_rep)
        
        
        tuple=[var_digit.get(i, i) for i in numlist]
        
        sum_tuple= int(tuple[0])*10 +int(tuple[len(tuple)-1])
        
        sum= int(sum)+ int(sum_tuple)
        
        
    return sum
    

print(day1func(inputval))
            
        
