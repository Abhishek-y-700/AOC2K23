import re

var_digit = { "one":1 , "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8,"nine":9 }
example = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]
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

