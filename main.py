import sys

if __name__ == "__main__":
    tree = "T"
    empty = "."
    mushroom = "+"
    water = "~"
    rock = "R"
    laro = "L"
    pickaxe = "x"
    flamethrower = "*"
    
    # the quantity per object will be randomized
    global num_mushrooms, num_trees, num_fire, num_water, num_pickaxe, num_rock
    num_mushrooms = ...
    collected_mushrooms = ...
    num_trees = ...
    num_fire = ...
    num_water = ...
    num_pickaxe = ...
    num_rock = ...
    
    winning_message = "olanap lodicakes"
    
    # initialize the grid
    grid = []
    
    def ending_screen() -> None:
        
    
    # if the current location of Laro has a mushroom, then 
    # (1) pick it up
    # (2) change the mushroom to an empty space
    # (3) decrease the total number of mushrooms
    def is_mushroom(i, j):
        if grid[i][j] = mushroom:
            grid[i][j] = empty
            num_mushrooms -= 1
            collected_mushrooms += 1
            if num_mushrooms == 0:
                print(winning_message)
                ending_screen()
                
    def is_rock