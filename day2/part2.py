import re

with open("input.txt", "r") as f:
    ranges = [r.strip() for r in f.read().split(",") if r.strip() != ""]

invalids = []

for rng in ranges:
    (start, end) = rng.split("-")

    for i in range(int(start), int(end) + 1):
        numstr = str(i)

        match = re.fullmatch("(\\d+)\\1+", numstr)

        if match:
            # print(f"invalid: {i}")
            invalids.append(i)

total = 0
for iid in invalids:
    total += iid

print(f"Part 2: Sum of invalid IDs: {total}")
