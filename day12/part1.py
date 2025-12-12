with open("input.txt", "r") as f:
    parts = f.read().split("\n\n")

    regiontexts = "".join(parts[-1:])
    shapetexts = parts[:-1]

    shapes = []
    for shapetext in shapetexts:
        lines = shapetext.split("\n")
        del lines[0]
        shapes.append((sum([a.count("#") for a in lines]), lines))

    print(shapes)

    regions = []
    for regiontext in regiontexts.split("\n"):
        regionparts = regiontext.split(":")

        w, h = [int(v) for v in regionparts[0].split("x")]
        presentspec = [int(p.strip()) for p in regionparts[1].strip().split(" ")]
        regions.append((w, h, w * h, presentspec))

    print(regions)

goodregions = 0
for region in regions:
    w, h, area, spec = region

    totalarea = 0
    for shapeindex, shapespec in enumerate(spec):
        # totalarea += shapes[shapeindex][0] * shapespec
        totalarea += 9 * shapespec

    if totalarea > area:
        # print("Way too big (worst case)")
        pass
    else:
        print(f"Not worst case at least {w}x{h}")
        goodregions += 1

print(goodregions)
