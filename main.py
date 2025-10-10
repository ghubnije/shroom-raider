# NOTES:
# (i, j) will denote the row (top-bottom) and column (left-right) of Laro

import sys
import random

# TEST
# create an r x c grid
r, c = map(int, input().split())

# initialization of characters in the grid will follow the same order here
characters = {
    "empty": ".",
    "tree": "T",
    "mushroom": "+",
    "water": "~",
    "rock": "R",
    "laro": "L",
    "pickaxe": "x",
    "flamethrower": "*",
    "paved tile": "-"
}

# the quantity of the mushrooms will be randomized
total_characters = r * c
total_free = total_characters - (2 * (r + c) - 4)
collected_mushrooms = 0
curr_location = []

num_laro = 1
num_mushrooms = random.randint(1, max((r * c) // 10, 1))
num_trees = random.randint(0, (total_free - num_laro) // 2)
num_water = random.randint(0, (total_free - num_mushrooms - num_trees) // 4)
num_rock = random.randint(0, (total_free - num_mushrooms - num_water - num_trees) // 4)
num_pickaxe = random.randint(
    0, (total_free - num_mushrooms - num_water - num_trees - num_rock) // 10
)
num_flamethrower = random.randint(
    0,
    (total_free - num_mushrooms - num_water - num_trees - num_rock - num_pickaxe) // 10,
)

winning_message = "olanap lodicakes"
losing_message = "bobo lmao"


def is_edge(y: int, x: int) -> bool:
    return (y in (0, r - 1) and 0 <= x < c) or (x in (0, c - 1) and 0 <= y < c)


def is_inside(y: int, x: int) -> bool:
    return 0 <= y < r and 0 <= x < c


# TODO: verify that game is playable given the mushrooms and trees.
# it is possible that the game is not winnable if there are say less pickaxes than trees covering the mushrooms


def init_grid():
    # initialize the grid
    grid = [list("T" if is_edge(R, C) else "." for C in range(c)) for R in range(r)]
    coords = []

    def gen_coordinates_for_item(quantity: int, coordinates=None, coords=coords):

        if coordinates == None:
            coordinates = []

        if len(coordinates) == quantity:
            return coordinates

        coordinate = [random.randint(1, r - 2), random.randint(1, c - 2)]

        if coordinate in coords:
            return gen_coordinates_for_item(quantity, coordinates)
        else:
            coordinates.append(coordinate)
            return gen_coordinates_for_item(quantity, coordinates)

    laro = gen_coordinates_for_item(num_laro)
    coords.extend(laro)
    curr_location.append(laro[0])

    mushrooms = gen_coordinates_for_item(num_mushrooms)
    coords.extend(mushrooms)

    trees = gen_coordinates_for_item(num_trees)
    coords.extend(trees)

    waters = gen_coordinates_for_item(num_water)
    coords.extend(waters)

    rocks = gen_coordinates_for_item(num_rock)
    coords.extend(rocks)

    pickaxes = gen_coordinates_for_item(num_pickaxe)
    coords.extend(pickaxes)

    flamethrowers = gen_coordinates_for_item(num_flamethrower)
    coords.extend(flamethrowers)

    print(f"coords = {coords}")

    # TODO: Convert these into a function for abstraction
    for l in laro:
        y, x = l
        grid[y][x] = characters["laro"]

    for mushroom in mushrooms:
        y, x = mushroom
        grid[y][x] = characters["mushroom"]

    for tree in trees:
        y, x = tree
        grid[y][x] = characters["tree"]

    for water in waters:
        y, x = water
        grid[y][x] = characters["water"]

    for rock in rocks:
        y, x = rock
        grid[y][x] = characters["rock"]

    for pickaxe in pickaxes:
        y, x = pickaxe
        grid[y][x] = characters["pickaxe"]

    for flamethrower in flamethrowers:
        y, x = flamethrower
        grid[y][x] = characters["flamethrower"]

    return grid


grid = init_grid()

def print_grid():
    global grid
    for subgrid in grid:
        print(subgrid)
        
i, j = curr_location[0]

def ending_screen(status: str) -> None:
    if status == "win":
        print(winning_message)
    elif status == "lose":
        print(losing_message)
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


def determine_object(y, x) -> str:
    if grid[y][x] == characters["empty"]:
        return "empty"
    elif grid[y][x] == characters["mushroom"]:
        return "mushroom"
    elif grid[y][x] == characters["tree"]:
        return "tree"
    elif grid[y][x] == characters["flamethrower"]:
        return "flamethrower"
    elif grid[y][x] == characters["pickaxe"]:
        return "pickaxe"
    elif grid[y][x] == characters["rock"]:
        return "rock"
    elif grid[y][x] == characters["water"]:
        return "water"
    else:
        return ""


# if the current location of Laro has a mushroom, then
# (1) pick it up
# (2) change the mushroom to an empty space
# (3) decrease the total number of mushrooms
def do_mushroom(
    i: int,
    j: int,
    y: int,
    x: int,
):
    global num_mushrooms, collected_mushrooms, grid
    grid[y][x] = characters["empty"]
    grid[i][j] = characters["empty"]
    num_mushrooms -= 1
    collected_mushrooms += 1
    if num_mushrooms == 0:
        ending_screen("win")

    return [y, x]


def do_rock(i: int, j: int, y: int, x: int):
    global grid
    direction = get_direction(i, j, y, x)
    print(f"direction = {direction}")

    if direction == "up" and grid[y + 1][x] in (characters["water"], characters["empty"], characters["paved tile"]):
        grid[i][j] = characters["empty"]
        grid[y][x] = characters["laro"]
        grid[y + 1][x] = characters["rock"]
    elif direction == "down" and grid[y - 1][x] in (characters["water"], characters["empty"], characters["paved tile"]):
        grid[i][j] = characters["empty"]
        grid[y][x] = characters["laro"]
        grid[y - 1][x] = characters["rock"]
    elif direction == "left" and grid[y][x + 1] in (characters["water"], characters["empty"], characters["paved tile"]):
        grid[i][j] = characters["empty"]
        grid[y][x] = characters["laro"]
        grid[y][x + 1] = characters["rock"]
    elif direction == "right" and grid[y][x - 1] in (characters["water"], characters["empty"], characters["paved tile"]):
        grid[i][j] = characters["empty"]
        grid[y][x] = characters["laro"]
        grid[y][x - 1] = characters["rock"]

    return [y, x]


def do_tree():
    global i, j
    return [i, j]


def do_water() -> None:
    ending_screen("lose")


def do_empty(i: int, j: int, y: int, x: int) -> list:
    global grid
    grid[y][x] = characters["laro"]
    grid[i][j] = characters["empty"]
    return [y, x]


def get_user_input(commands: str):
    global i, j, curr_location, item, x, y
    for cmd in commands:
        print_grid()
        if cmd.lower() in ("w"):
            y = i - 1
            x = j
            item = determine_object(y, x)
        
        elif cmd.lower() in ('s'):
            y = i + 1
            x = j
            item = determine_object(y, x)
            
        print(f"item = {item}")
        print(f"i = {i}, j = {j}\ny = {y}, x = {x}\n")
            
        if item == "empty":
            curr_location = do_empty(i, j, y, x)
        elif item == "mushroom":
            curr_location = do_mushroom(i, j, y, x)
        elif item == "rock":
            curr_location = do_rock(i, j, y, x)
        elif item == "tree":
            curr_location = do_tree()
        elif item == "water":
            do_water()
        
        i, j = curr_location
        
        print(f"current location = {curr_location}")


get_user_input("wwwss")
