import math

class Day91:
    def __init__(self):
        self.coords = set()
        with open("input.txt", "r") as f:
            for line in f.readlines():
                if line.strip() == "": continue
                parts = [int(x) for x in line.split(",")]
                self.coords.add((parts[0], parts[1]))


    def distance_squared(self, a, b) -> float:
        dx = a[0] - b[0]
        dy = a[1] - b[1]
        return dx * dx + dy * dy

    def distance_to(self, a, b) -> float:
        return math.sqrt(self.distance_squared(a, b))
    

    def process(self):
        pairs = set()
        # just do the same thing as day 8!
        for i, tile in enumerate(self.coords):
            for j, other in enumerate(self.coords):
                if i >= j:
                    continue

                distance = self.distance_to(tile, other)
                pairs.add((distance, tile, other))

        pairs = sorted(pairs, key=lambda p: p[0])
        pairs.reverse()

        largest = 0
        for corners in pairs:
            distance, a, b = corners
            ax, ay = a
            bx, by = b

            x = abs(ax - bx) + 1
            y = abs(ay - by) + 1

            area = x*y
            print(area)
            if area > largest:
                largest = area

        print(largest)

if __name__ == "__main__":
    day9 = Day91()
    day9.process()
