with open("input.txt", "r") as f:
    parts = f.read().split("\n\n")

allranges = [r.strip() for r in parts[0].split("\n") if r.strip() != ""]

ranges = []

for ra in allranges:
    limits = ra.split("-")
    ranges.append((int(limits[0]), int(limits[1])))

# sort by min
ranges = sorted(ranges, key=lambda range: range[0])

min = ranges[0][0]
max = ranges[0][1]
finalranges = []

for i, range in enumerate(ranges):
    thismin = range[0]
    thismax = range[1]

    # handle edge case where this range is totally inside the current ranges
    if thismin >= min and thismax <= max:
        continue

    if thismin <= max:
        max = thismax
    else:
        finalranges.append((min, max))
        min = thismin
        max = thismax

finalranges.append((min, max))

total = 0
for r in finalranges:
    total += (r[1] - r[0]) + 1

print(f"Total: {total} (Ranges: {len(finalranges)})")
