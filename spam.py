import re
with open('inputd1p1.txt','r')as file:
        file_content=file.read()
        inputval=(file_content).splitlines() #splits to list
var_digit = { "one":1 , "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8,"nine":9 }
example = ["eightwothreeoneighttwone","onetwoneight"]
sum=0
for char in inputval:
    
    char_rep= re.sub('eightwo', 'eighttwo', char, re.I)
    char_rep= re.sub('oneight', 'oneeight', char_rep, re.I)
    char_rep= re.sub('twone', 'twoone', char_rep, re.I)

    #oneight 

    numlist = re.findall(r'(\d|one|two|three|four|five|six|seven|eight|nine)', char_rep)
    print(numlist)
    print([var_digit.get(i, i) for i in numlist])
    tuple=[var_digit.get(i, i) for i in numlist]
    
    sum_tuple= int(tuple[0])*10 +int(tuple[len(tuple)-1])
    print(sum_tuple)
    sum= sum+ sum_tuple
    print(sum  ) 
    print('End func')

