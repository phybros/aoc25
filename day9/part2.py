class Day92:
    def __init__(self):
        self.coords = []
        with open("input.txt", "r") as f:
            for line in f.readlines():
                if line.strip() == "":
                    continue
                parts = [int(x) for x in line.split(",")]
                self.coords.append((parts[0], parts[1]))

    def segments_intersect(self, p1, p2, p3, p4):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4

        seg1_horizontal = y1 == y2
        seg2_horizontal = y3 == y4

        # both horizontal - parallel, can't cross
        if seg1_horizontal and seg2_horizontal:
            return False

        # both vertical - parallel, can't cross
        if not seg1_horizontal and not seg2_horizontal:
            return False

        # one horizontal, one vertical - make sure seg1 is horizontal
        if not seg1_horizontal:
            # swap them
            x1, y1, x2, y2, x3, y3, x4, y4 = x3, y3, x4, y4, x1, y1, x2, y2

        # seg1 is horizontal, seg2 is vertical
        horiz_y = y1
        horiz_minx = min(x1, x2)
        horiz_maxx = max(x1, x2)

        vert_x = x3
        vert_miny = min(y3, y4)
        vert_maxy = max(y3, y4)

        if horiz_minx < vert_x < horiz_maxx:
            if vert_miny < horiz_y < vert_maxy:
                return True

        return False

    def point_on_edge(self, point, polygon):
        x, y = point

        for i in range(len(polygon)):
            p1 = polygon[i]
            p2 = polygon[(i + 1) % len(polygon)]

            x1, y1 = p1
            x2, y2 = p2

            # Horizontal edge
            if y1 == y2 == y:
                if min(x1, x2) <= x <= max(x1, x2):
                    return True

            # Vertical edge
            if x1 == x2 == x:
                if min(y1, y2) <= y <= max(y1, y2):
                    return True

        return False

    def any_edges_cross(self, rectedges, polyedges):
        for rectedge in rectedges:
            for polyedge in polyedges:
                # unpack the tuples!
                if self.segments_intersect(*rectedge, *polyedge):
                    return True
        return False

    def point_in_polygon(self, point, polygon):
        x, y = point
        crossings = 0

        for i in range(len(polygon)):
            p1 = polygon[i]
            p2 = polygon[(i + 1) % len(polygon)]

            x1, y1 = p1
            x2, y2 = p2

            # We only care about vertical edges (horizontal edges can't cross a horizontal ray)
            if x1 != x2:
                continue

            # The vertical edge is at x = x1
            edge_x = x1
            edge_miny = min(y1, y2)
            edge_maxy = max(y1, y2)

            # Is the edge to the RIGHT of our point?
            if edge_x <= x:
                continue

            # Does our ray (at height y) pass through this edge?
            if edge_miny < y < edge_maxy:
                crossings += 1

        return crossings % 2 == 1

    def process(self):
        rectangles = set()
        for i, tile in enumerate(self.coords):
            for j, other in enumerate(self.coords):
                if i >= j:
                    continue

                ax, ay = tile
                bx, by = other

                x = abs(ax - bx) + 1
                y = abs(ay - by) + 1

                area = x * y
                rectangles.add((area, tile, other))

        rectangles = sorted(rectangles, key=lambda p: p[0])
        rectangles.reverse()

        self.edges = []
        for i in range(len(self.coords)):
            thiscoord = self.coords[i]
            nextindex = i + 1
            if nextindex >= len(self.coords):
                nextindex = 0
            nextcoord = self.coords[nextindex]
            self.edges.append((thiscoord, nextcoord))

        largest_rect = (0, 0, 0)
        for i, rectangle in enumerate(rectangles):
            contained = True
            area, a, b = rectangle
            ax, ay = a
            bx, by = b

            minx, maxx = min(ax, bx), max(ax, bx)
            miny, maxy = min(ay, by), max(ay, by)
            corners = [(minx, miny), (maxx, miny), (maxx, maxy), (minx, maxy)]

            rectedges = [
                (corners[0], corners[1]),
                (corners[1], corners[2]),
                (corners[2], corners[3]),
                (corners[3], corners[0]),
            ]

            for corner in corners:
                if corner not in self.coords:
                    if not self.point_in_polygon(
                        corner, self.coords
                    ) and not self.point_on_edge(corner, self.coords):
                        contained = False
                        break
            if contained:
                for edge in rectedges:
                    mid = (
                        (edge[0][0] + edge[1][0]) // 2,
                        (edge[0][1] + edge[1][1]) // 2,
                    )
                    if mid not in self.coords:
                        if not self.point_in_polygon(
                            mid, self.coords
                        ) and not self.point_on_edge(mid, self.coords):
                            contained = False
                            break
            if self.any_edges_cross(rectedges, self.edges):
                contained = False

            if contained:
                if area > largest_rect[0]:
                    largest_rect = rectangle

        print(f"Largest Rectangle: {largest_rect}")


if __name__ == "__main__":
    day9 = Day92()
    day9.process()
