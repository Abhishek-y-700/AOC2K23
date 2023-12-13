# AOC 2k23 D2 P2
#Cube Conundrum
import re
with open('d2ip.txt','r')as file:
    file_content=file.read()
    inputval=(file_content).splitlines() #splits to list

# possibility = 12 red cubes, 13 green cubes, and 14 blue cubes
# '\b([1-9]|1[0-2])\b\sred'gi to find red 12 |  ([1][0-2]\sred) | red_pat=r'([1][0-2]|[1-9])\sred'
def cubes(inp):
    
    game_no=0
    sum=0
    for game in inp:
        game_no+=1

        red_pat=r'(\d{2}|\d)\sred'
        green_pat=r'(\d{2}|\d)\sgreen'
        blue_pat=r'(\d{2}|\d)\sblue'
        
        red_balls= re.findall(red_pat,game)
        green_balls= re.findall(green_pat,game)
        blue_balls= re.findall(blue_pat,game)
        
        red=limit_func(red_balls)
        
        green=limit_func(green_balls)

        blue=limit_func(blue_balls)

        power = red*green*blue
        """ print(power) """
        sum+=power
        if game_no==100:
            print(sum)
    


        

        
def limit_func(set):
    """ print("Set is:",set) """
    largest=int(set[0])
    for i in set:
        if int(i)>largest:
            largest = int(i)

    return largest

    

cubes(inputval)