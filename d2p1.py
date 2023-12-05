# AOC 2k23 D2 P1
#Cube Conundrum
import re
with open('d2ip.txt','r')as file:
    file_content=file.read()
    inputval=(file_content).splitlines() #splits to list

# possibility = 12 red cubes, 13 green cubes, and 14 blue cubes
# '\b([1-9]|1[0-2])\b\sred'gi to find red 12 | red= re.findall(r'(`\b([1-9]|1[0-2])\b\sred`ig)',game)
def cubes(inp):
    red= 12
    green=13
    blue=14
    game_no=0
    for game in inp:
        game_no+=1
        red= re.findall(r'([1-9]|1[0-2])\sred',game)
        print(red)
        

cubes(inputval)