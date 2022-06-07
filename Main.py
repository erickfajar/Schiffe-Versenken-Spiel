from dis import show_code
from sqlite3 import Row
from Coordinate import Coordinate
#Attributes
player_turn = 1
number_ship = 3
loop = True


coordinate_map = Coordinate()

# map size input
while loop :
    try: 
        user_input = input("enter the grid size : ")
        grid_size = int(user_input)
        if grid_size >= 5 and grid_size <= 10 : 
            break
        else : 
            print ("input must be between 5 and 10 \n")

    except ValueError: 
        print ("please input a valid number")
