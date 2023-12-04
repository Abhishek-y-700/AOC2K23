import re

with open('inputd1p1.txt','r')as file:
    file_content=file.read()
    inputval=(file_content).splitlines() #splits to list

var_digit = { "one":1 , "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8,"nine":9 }
example = ["eightwothreeoneighttwone","onetwoneight"]

def subs(inputtt):
    list_new=[]
    for x in inputtt:
        char_rep= re.sub('one', 'o1e', x, re.I)
        char_rep= re.sub('two', 't2o', char_rep, re.I)
        char_rep= re.sub('three', 't3e', char_rep, re.I)
        char_rep= re.sub('four', 'f4r', char_rep, re.I)
        char_rep= re.sub('five', 'f5e', char_rep, re.I)
        char_rep= re.sub('six', 's6x', char_rep, re.I)
        char_rep= re.sub('seven', 's7n', char_rep, re.I)
        char_rep= re.sub('eight', 'e8t', char_rep, re.I)
        char_rep= re.sub('nine', 'n9e', char_rep, re.I)
        list_new.append(str(char_rep))

    return list_new

subs_calc=subs(inputval)

def mainfunc(subs_calc):
    sum=0
    for char in subs(subs_calc):
        numlist = re.findall('(?=(one|two|three|four|five|six|seven|eight|nine|\d))', char)

        print(numlist)
        print([var_digit.get(i, i) for i in numlist])
        tuple=[var_digit.get(i, i) for i in numlist]
        
        sum_tuple= int(tuple[0])*10 +int(tuple[len(tuple)-1])
        print(sum_tuple)
        sum= sum+ sum_tuple
        print(sum) 
        print('End func')
    return sum  # Moved outside of the for loop

print(mainfunc(subs_calc))
