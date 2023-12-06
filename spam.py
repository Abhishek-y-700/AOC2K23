# AOC 2k23 D2 P1
#Cube Conundrum
import re
with open('d2ip.txt','r')as file:
    file_content=file.read()
    inputval=(file_content).splitlines() #splits to list

# possibility = 12 red cubes, 13 green cubes, and 14 blue cubes
# '\b([1-9]|1[0-2])\b\sred'gi to find red 12 | red= re.findall(r'(`\b([1-9]|1[0-2])\b\sred`ig)',game)
def cubes(inp):
    red =["1 red"]
    """ red= 12
    green=13
    blue=14 """
    red_pat=r'(\d\d\sred)|(\d\sred)'
    game_no=0
    sum=0
    for game in inp:
        red = []
        
        game_no+=1
        
        red_pat=r'([0-1][0-2])\sred|\d\sred'
        red=re.findall(red_pat,game)
        print(red)
        
        if any(int for x in red):
            print(" This set of values is Accepted")
        else:
            print(" This set has no acceptable value for red balls")

        
        

cubes(inputval)