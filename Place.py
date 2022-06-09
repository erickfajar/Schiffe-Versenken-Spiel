class Place:
    def place_ship(self, orientation,row ,column , grid_player):
       # vertical 
        if orientation == "v" :
            grid_player [row][column] = "1"
            grid_player [row][column+1] = "1"
            grid_player [row][column+2] = "1"

        # horizontal
        if orientation == "h" : 
            grid_player [row][column] = "1"    
            grid_player [row+1][column] = "1"
            grid_player [row+2][column] = "1"