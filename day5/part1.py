with open("input.txt", "r") as f:
    parts = f.read().split("\n\n")

allranges = [r.strip() for r in parts[0].split("\n") if r.strip() != ""]
foods = [r.strip() for r in parts[1].split("\n") if r.strip() != ""]

ranges = []
freshfoods = []

for ra in allranges:
    limits = ra.split("-")
    ranges.append((int(limits[0]), int(limits[1])))

for food in foods:
    fresh = False
    foodint = int(food)

    for r in ranges:
        if foodint >= r[0] and foodint <= r[1]:
            fresh = True
            freshfoods.append(food)
            print(f"Food {foodint} is fresh")
            break

    if not fresh:
        print(f"Food {food} was spoiled SAD")

print(f"Total Fresh: {len(freshfoods)}")
