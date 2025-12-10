class Day92:
    def __init__(self):
        self.coords = []
        with open("input.txt", "r") as f:
            for line in f.readlines():
                if line.strip() == "":
                    continue
                parts = [int(x) for x in line.split(",")]
                self.coords.append((parts[0], parts[1]))

        # Convert to set for O(1) membership checks
        self.coords_set = set(self.coords)

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

        # Check horizontal edges
        for edge_y, minx, maxx in self.horiz_edges:
            if edge_y == y and minx <= x <= maxx:
                return True

        # Check vertical edges
        for edge_x, miny, maxy in self.vert_edges:
            if edge_x == x and miny <= y <= maxy:
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

        # Use pre-computed vertical edges
        for p1, p2 in self.vertical_edges:
            edge_x = p1[0]  # Both points have same x (vertical edge)
            edge_miny = min(p1[1], p2[1])
            edge_maxy = max(p1[1], p2[1])

            # Is the edge to the RIGHT of our point and does our ray pass through it?
            if edge_x > x and edge_miny < y < edge_maxy:
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

        rectangles = sorted(rectangles, key=lambda p: p[0], reverse=True)

        # Build polygon edges
        self.edges = [
            (self.coords[i], self.coords[(i + 1) % len(self.coords)])
            for i in range(len(self.coords))
        ]

        # Pre-compute vertical edges for point_in_polygon (only uses vertical edges)
        self.vertical_edges = [
            (p1, p2) for p1, p2 in self.edges if p1[0] == p2[0]
        ]

        # Pre-compute horizontal edges with bounds for faster point_on_edge
        self.horiz_edges = []
        for p1, p2 in self.edges:
            if p1[1] == p2[1]:  # Horizontal edge
                y = p1[1]
                minx = min(p1[0], p2[0])
                maxx = max(p1[0], p2[0])
                self.horiz_edges.append((y, minx, maxx))

        # Pre-compute vertical edges with bounds for faster point_on_edge
        self.vert_edges = []
        for p1, p2 in self.edges:
            if p1[0] == p2[0]:  # Vertical edge
                x = p1[0]
                miny = min(p1[1], p2[1])
                maxy = max(p1[1], p2[1])
                self.vert_edges.append((x, miny, maxy))

        largest_rect = (0, 0, 0)
        for rectangle in rectangles:
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

            # Check corners first (fast fail on first bad corner)
            contained = True
            for point in corners:
                if point in self.coords_set:
                    continue

                px, py = point

                # Inline point_in_polygon check (using pre-computed bounds)
                crossings = 0
                for edge_x, edge_miny, edge_maxy in self.vert_edges:
                    if edge_x > px and edge_miny < py < edge_maxy:
                        crossings += 1

                in_polygon = crossings % 2 == 1

                # If not in polygon, check if on edge
                if not in_polygon:
                    on_edge = False
                    for edge_y, minx, maxx in self.horiz_edges:
                        if edge_y == py and minx <= px <= maxx:
                            on_edge = True
                            break
                    if not on_edge:
                        for edge_x, miny, maxy in self.vert_edges:
                            if edge_x == px and miny <= py <= maxy:
                                on_edge = True
                                break

                    if not on_edge:
                        contained = False
                        break

            # Check edge midpoints if corners passed
            if contained:
                for edge in rectedges:
                    point = (
                        (edge[0][0] + edge[1][0]) // 2,
                        (edge[0][1] + edge[1][1]) // 2,
                    )
                    if point in self.coords_set:
                        continue

                    px, py = point

                    # Inline point_in_polygon check (using pre-computed bounds)
                    crossings = 0
                    for edge_x, edge_miny, edge_maxy in self.vert_edges:
                        if edge_x > px and edge_miny < py < edge_maxy:
                            crossings += 1

                    in_polygon = crossings % 2 == 1

                    # If not in polygon, check if on edge
                    if not in_polygon:
                        on_edge = False
                        for edge_y, minx, maxx in self.horiz_edges:
                            if edge_y == py and minx <= px <= maxx:
                                on_edge = True
                                break
                        if not on_edge:
                            for edge_x, miny, maxy in self.vert_edges:
                                if edge_x == px and miny <= py <= maxy:
                                    on_edge = True
                                    break

                        if not on_edge:
                            contained = False
                            break

            # Check edge crossings last
            if contained and self.any_edges_cross(rectedges, self.edges):
                contained = False

            if contained:
                largest_rect = rectangle
                # Early termination: rectangles are sorted largest first
                break

        print(f"Largest Rectangle: {largest_rect}")


if __name__ == "__main__":
    day9 = Day92()
    day9.process()
