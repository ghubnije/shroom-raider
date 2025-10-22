r, c = 8, 8

characters = {
    "empty": ".",
    "tree": "T",
    "mushroom": "+",
    "water": "~",
    "rock": "R",
    "laro": "L",
    "pickaxe": "x",
    "flamethrower": "*",
    "paved tile": "-",
}

def is_edge(y: int, x: int) -> bool:
    return y in (0, r - 1) or x in (0, c - 1)

def init_grid(r, c, characters):
    grid = [list("T" if is_edge(R, C) else "." for C in range(c)) for R in range(r)]
    
    laro = [3, 4]
    
    return grid, laro

grid = init_grid(r, c, characters)
for subgrid in grid[0]:
    print(subgrid)