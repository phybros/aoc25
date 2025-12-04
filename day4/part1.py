import copy

with open("input2.txt", "r") as f:
    lines = [r.strip() for r in f.read().split("\n") if r.strip() != ""]

grid = []
width = 0
height = 0
accessible = []

for row in lines:
    height += 1
    cols = []

    if len(row) > width:
        width = len(row)

    for col in row:
        cols.append(col)
    grid.append(cols)

print(f"grid {width}x{height}")

for y in range(0, height):
    for x in range(0, width):
        neighnum = 0

        if grid[y][x] != "@":
            continue

        for dx in range(-1, 2):
            for dy in range(-1, 2):

                # ignore self
                if dx == 0 and dy == 0:
                    continue

                if x + dx > width - 1:
                    continue

                if y + dy > height - 1:
                    continue

                if x + dx < 0:
                    continue

                if y + dy < 0:
                    continue

                if grid[y + dy][x + dx] == "@":
                    neighnum += 1

        if neighnum < 4:
            accessible.append((x, y))

print(f"Accessible rolls: {len(accessible)}")
