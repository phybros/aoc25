grid = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        grid.append(list(line.strip()))

for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
        if grid[y][x] == "^" or grid[y][x] == "S":
            continue

        if y - 1 >= 0:
            if grid[y-1][x] == "S" or grid[y-1][x] == "|":
                grid[y][x] = "|"
        
            if x - 1 >= 0:
                if grid[y][x-1] == "^" or grid[y-1][x-1] == "^":
                    grid[y][x] = "|"
        
            if x + 1 < len(grid[y]):
                if grid[y][x+1] == "^" or grid[y-1][x+1] == "^":
                    grid[y][x] = "|"


for row in grid:
    print("".join(row))

splits = 0

for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
        if grid[y][x] == "^" and grid[y-1][x] == "|":
            splits += 1

print(f"\nTotal Beam Splits: {splits}")
