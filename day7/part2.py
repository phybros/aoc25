grid = []
checks = {}
unique_splits = set()
unique_paths = []
unique_path_count = 0
splitters = {}

with open("input.txt", "r") as f:
    lines = f.readlines()
    for y in range(0, len(lines)):
        row = []
        for x in range(0, len(lines[y])):
            if lines[y][x].strip() != "":
                row.append(lines[y][x])

                if lines[y][x] == "^":
                    splitters[(y,x)] = "LR"

        grid.append(row)

def printgrid():
    for row in grid:
        print("".join(row))

def emitbeam(y, x, path):
    global unique_path_count
    ycheck = 0
    hit = False
    while not hit:
        # reached the end
        if y+ycheck > len(grid) - 1:
            # print(f"Reached bottom {path}")
            # unique_paths.append(path)
            unique_path_count += 1
            if unique_path_count % 1000000 == 0:
                print(f"Paths: {unique_path_count}, Current Path: {path}")
            break

        hit = grid[y+ycheck][x] == "^"
        # reached another splitter, send off some beams
        if hit:
            emitbeam(y+ycheck, x-1, path + "L")
            emitbeam(y+ycheck, x+1, path + "R")
        
        ycheck += 1



for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
        if grid[y][x] == "S":
            emitbeam(y, x, "")

# i = 1
# for p in unique_paths:
#     print(f"{i}: {p}")
#     i+=1
print(unique_path_count)
    #     if x + 1 < len(grid[y]):
    #         if grid[y][x+1] == "^" and "L" in splitters[(y,x+1)]:
    #             emitbeam(y, x)
    #             splitters[(y,x+1)] = splitters[(y,x+1)].strip("L")

    #     if x - 1 >= 0:
    #         if grid[y][x-1] == "^" and "R" in splitters[(y,x-1)]:
    #             emitbeam(y, x)
    #             splitters[(y,x-1)] = splitters[(y,x-1)].strip("R")
        
    # printgrid()

# print(splitters)
# print(len(unique_splits))



# print(totalsplitters)

# for y in range(0, len(grid)):
#     for x in range(0, len(grid[y])):
#         if grid[y][x] == "^" or grid[y][x] == "S":
#             checks[(y,x)] = 0
#             continue

#         if y - 1 >= 0:
#             if grid[y-1][x] == "S" or grid[y-1][x] == "|":
#                 grid[y][x] = "|"
        
            

#             if x - 1 >= 0:
#                 if grid[y][x-1] == "^" or grid[y-1][x-1] == "^":
#                     grid[y][x] = "|"
        
#             if x + 1 < len(grid[y]):
#                 if grid[y][x+1] == "^" or grid[y-1][x+1] == "^":
#                     grid[y][x] = "|"

# print(checks)


# done = False

# while not done:
#     for y in range(0, len(grid)):
#         for x in range(0, len(grid[y])):
#             if grid[y][x] == "^" and grid[y-1][x] == "|":
#                 splits += 1

# print(f"\nTotal Beam Splits: {splits}")
