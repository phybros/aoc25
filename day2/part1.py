with open("input.txt", "r") as f:
    ranges = [r.strip() for r in f.read().split(",") if r.strip() != ""]

invalidids = []

for rng in ranges:
    (start, end) = rng.split("-")

    for i in range(int(start), int(end) + 1):
        numstr = str(i)

        if len(numstr) % 2 != 0:
            continue

        step = int(len(numstr) / 2)
        out = [(numstr[i : i + step]) for i in range(0, len(numstr), step)]

        if out[0] == out[1]:
            invalidids.append(i)

total = 0
for iid in invalidids:
    total += iid

print(f"Part 1: Sum of invalid IDs: {total}")
