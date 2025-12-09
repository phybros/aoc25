import math

class Day92:
    def __init__(self):
        minx = 999999999999999
        miny = 999999999999999
        maxx = 0
        maxy = 0
        self.coords = []
        with open("input.txt", "r") as f:
            for line in f.readlines():
                if line.strip() == "": continue
                parts = [int(x) for x in line.split(",")]
                self.coords.append((parts[0], parts[1]))

                if parts[0] < minx:
                    minx = parts[0]
                if parts[1] < miny:
                    miny = parts[1]
                if parts[0] > maxx:
                    maxx = parts[0]
                if parts[1] > maxy:
                    maxy = parts[1]

        # for y in range(miny-1, maxy + 2):
        #     for x in range(minx-1, maxx + 2):
        #         tile = False
        #         inside = self.point_in_polygon((x,y), self.coords) or self.point_on_edge((x,y), self.coords)
        #         for xy in self.coords:
        #             if x == xy[0] and y == xy[1]:
        #                 tile = True

        #         if tile:
        #             print("#", end="")
        #         else:
        #             if inside:
        #                 print("X", end="")
        #             else:
        #                 print(".", end="")
        #     print()

    def point_on_edge(self, point, vertices):
        x, y = point
        n = len(vertices)
        
        for i in range(n):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % n]
            
            # Check if point is on segment (x1,y1) to (x2,y2)
            if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
                # Check collinearity using cross product
                cross = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)
                if cross == 0:
                    return True
        
        return False

    def point_in_polygon(self, point, vertices):
        x, y = point
        n = len(vertices)
        inside = False
        
        j = n - 1
        for i in range(n):
            xi, yi = vertices[i]
            xj, yj = vertices[j]
            
            if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
                inside = not inside
            j = i
        
        return inside

    def order_points(self, points):
        cx = sum(p[0] for p in points) / len(points)
        cy = sum(p[1] for p in points) / len(points)
        
        def angle(p):
            return math.atan2(p[1] - cy, p[0] - cx)
        
        return sorted(points, key=angle)

    def polygon_area(self, vertices):
        n = len(vertices)
        area = 0
        for i in range(n):
            j = (i + 1) % n
            area += vertices[i][0] * vertices[j][1]
            area -= vertices[j][0] * vertices[i][1]
        return abs(area) / 2

    def distance_squared(self, a, b) -> float:
        dx = a[0] - b[0]
        dy = a[1] - b[1]
        return dx * dx + dy * dy

    def distance_to(self, a, b) -> float:
        return math.sqrt(self.distance_squared(a, b))
    
    def boundary_points(self, vertices):
        from math import gcd
        b = 0
        n = len(vertices)
        for i in range(n):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % n]
            b += gcd(abs(x2 - x1), abs(y2 - y1))
        return b

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
            print(corners)
            distance, a, b = corners
            ax, ay = a
            bx, by = b

            invalid = False
            for y in range(min(ay, by), max(ay, by)):
                if invalid:
                    break
                print(y)
                for x in range(min(ax, bx), max(ax, bx)):
                    if invalid:
                        break
                    if not self.point_in_polygon((x, y), self.coords) and not self.point_on_edge((x, y), self.coords):
                        invalid = True
                        break
            
            if not invalid:
                x = abs(ax - bx) + 1
                y = abs(ay - by) + 1

                area = x*y
                if area > largest:
                    largest = area
                    print(f"found new largest: {largest}")

        print(largest)

if __name__ == "__main__":
    day9 = Day92()
    day9.process()
