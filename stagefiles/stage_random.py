import random

def init_grid(r, c, characters):

    # the quantity of the mushrooms will be randomized
    total_characters = r * c
    total_free = total_characters - (2 * (r + c) - 4)
    collected_mushrooms = 0
    curr_location = []

    num_laro = 1
    num_mushrooms = random.randint(1, max((r * c) // 10, 1))
    num_trees = random.randint(0, (total_free - num_laro) // 2)
    num_water = random.randint(0, (total_free - num_mushrooms - num_trees) // 4)
    num_rock = random.randint(
        0, (total_free - num_mushrooms - num_water - num_trees) // 4
    )
    num_pickaxe = random.randint(
        0, (total_free - num_mushrooms - num_water - num_trees - num_rock) // 10
    )
    num_flamethrower = random.randint(
        0,
        (total_free - num_mushrooms - num_water - num_trees - num_rock - num_pickaxe)
        // 10,
    )

    def is_edge(y: int, x: int) -> bool:
        return y in (0, r - 1) or x in (0, c - 1)

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

    return grid, laro[0]