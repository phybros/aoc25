with open("input.txt", "r") as f:
    parts = f.read().split("\n\n")

allranges = [r.strip() for r in parts[0].split("\n") if r.strip() != ""]

unique_ids = set()
ranges = []
freshfoods = []
rangenum = 1

for ra in allranges:
    print(f"Processing range {rangenum}/{len(allranges)}...")
    limits = ra.split("-")
    for i in range(int(limits[0]), int(limits[1]) + 1):
        unique_ids.add(i)

print(len(unique_ids))
