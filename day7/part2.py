class Day7:
    def __init__(self):
        self.grid = []
        self.xstart = -1
        self.splitters = []

        with open("input.txt", "r") as f:
            lines = f.readlines()
            for y in range(0, len(lines)):
                row = []
                for x in range(0, len(lines[y])):
                    if lines[y][x].strip() != "":
                        row.append(lines[y][x])

                        if lines[y][x] == "^":
                            self.splitters.append((y, x))
                        if lines[y][x] == "S":
                            self.xstart = x
                self.grid.append(row)

    def next_splitter(self, x, fromy):
        for splitter in self.splitters:
            if splitter[0] > fromy:
                if splitter[1] == x:
                    return splitter

        return None

    def process(self):
        beams = {}
        for s in self.splitters:
            beams[s] = 0

        # get the first one
        first = self.next_splitter(self.xstart, 0)
        beams[first] = 1

        paths = 0
        for s in self.splitters:
            inbeams = beams[s]

            nextsplitterl = self.next_splitter(s[1] - 1, s[0])
            if nextsplitterl is not None:
                beams[nextsplitterl] += inbeams
            else:
                paths += inbeams

            nextsplitterr = self.next_splitter(s[1] + 1, s[0])
            if nextsplitterr is not None:
                beams[nextsplitterr] += inbeams
            else:
                paths += inbeams

        return paths


if __name__ == "__main__":
    day7 = Day7()
    print(f"Total Paths: {day7.process()}")
