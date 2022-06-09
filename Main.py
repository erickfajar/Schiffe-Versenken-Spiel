from Coordinate import Coordinate
from Place import Place



#Attributes
player_turn = 1
number_ship = 3
loop = True
game_over = False
grid = [[]]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"




    


coordinate_map = Coordinate()

def create_grid() :
    global grid_size
    global grid

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
    
    rows, cols = (grid_size, grid_size)

    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        grid.append(row)
def print_grid() :
    global grid
    global alphabet

    debug_mode = True

    alphabet = alphabet[0: len(grid) + 1]

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")


def main() :
    global game_over
    global grid_size


    print("welcome to battleships")

    # map size input
    create_grid()
    print_grid()

