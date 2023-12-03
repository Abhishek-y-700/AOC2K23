# Day 1  AOC 2k23
with open('inputd1p1.txt','r')as file:
        file_content=file.read()
        inputval=(file_content).splitlines() #splits to list


# Eg val inp
example= ["two1nine","eightwothree","three33"]
def day1func(example):
    sum=0
    var_digit={ "one":1 , "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8,"nine":9 }
    for x in example: 
        # Return first element two1nine= ["2","1","9"], then add index first and last
        #numlist = list(''.join(filter(str.isdigit, x)))
        for y in var_digit:           
          if y in x:
               print(" There exists a var digit")
        """ if any(char.isdigit() for char in x):  #To check presence of int digit
             print(" There exists an int digit") """
        print("End func")
    
    

print(day1func(example))
            
        