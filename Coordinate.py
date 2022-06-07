# prints a map grid
class Coordinate: 
    def show_coordinate (self, grid_size, grid_coordinate) :
        a = 0
        b = 0
        print(' ')
        while a < grid_size : 
            while b <grid_coordinate :
                print(grid_coordinate[a][b], end = ' ')
                b += 1
                print ("\n")
                b = 0
                a += 1
        print (" ")

    def ada () :
        print("aaaa")