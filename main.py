# NOTES:
# (i, j) will denote the row (top-bottom) and column (left-right) of Laro

import sys

characters = {
    "tree": "T",
    "empty": ".",
    "mushroom": "+",
    "water": "~",
    "rock": "R",
    "laro": "L",
    "pickaxe": "x",
    "flamethrower": "*",
}

# the quantity per object will be randomized
global num_mushrooms, num_trees, num_fire, num_water, num_pickaxe, num_rock
num_mushrooms = 1
collected_mushrooms = 0

winning_message = "olanap lodicakes"

# initialize the grid
grid = []


def ending_screen() -> None:
    print(winning_message)
    sys.exit(0)


# get the direction Laro came from when pushing or interacting with an object.
# y and x represents the row and column position of the object
def get_direction(i, j, y, x) -> str:
    di, dj = i - y, j - x
    if (di, dj) == (0, -1):
        direction = "left"
    elif (di, dj) == (0, 1):
        direction = "right"
    elif (di, dj) == (1, 0):
        direction = "down"
    else:
        direction = "up"

    return direction


# if the current location of Laro has a mushroom, then
# (1) pick it up
# (2) change the mushroom to an empty space
# (3) decrease the total number of mushrooms
def is_mushroom(
    i: int,
    j: int,
    y: int,
    x: int,
    collected_mushrooms: int = collected_mushrooms,
    num_mushrooms: int = num_mushrooms,
) -> None:
    if grid[y][x] == characters["mushroom"]:
        grid[y][x] = characters["empty"]
        grid[i][j] = characters["empty"]
        num_mushrooms -= 1
        collected_mushrooms += 1
        if num_mushrooms == 0:
            ending_screen()


def is_rock(i: int, j: int, y: int, x: int):
    if grid[y][x] == characters["rock"]:
        direction = get_direction(i, j, y, x)

        if direction == "up" and grid[y + 1][x] != characters["rock"]:
            grid[i][j] = characters["empty"]
            grid[y][x] = characters["laro"]
            grid[y + 1][x] = characters["rock"]
        elif direction == "down" and grid[y - 1][x] != characters["rock"]:
            grid[i][j] = characters["empty"]
            grid[y][x] = characters["laro"]
            grid[y - 1][x] = characters["rock"]
        elif direction == "left" and grid[y][x + 1] != characters["rock"]:
            grid[i][j] = characters["empty"]
            grid[y][x] = characters["laro"]
            grid[y][x + 1] = characters["rock"]
        elif direction == "right" and grid[y][x - 1] != characters["rock"]:
            grid[i][j] = characters["empty"]
            grid[y][x] = characters["laro"]
            grid[y][x - 1] = characters["rock"]
