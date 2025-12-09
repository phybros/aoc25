# so i can have a reference to Box inside Box
from __future__ import annotations
from array import array
import math


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.parent = None

    # dropping the sqrt when we only care about the relative distances
    # makes things a bit faster
    def distance_squared(self, other: Box) -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return dx * dx + dy * dy + dz * dz

    def distance_to(self, other: Box) -> float:
        return math.sqrt(self.distance_squared(other))

    def __repr__(self):
        return f"Box({self.x!r}, {self.y!r}, {self.z!r})"


class Day8:
    def __init__(self, boxes: list):
        self.boxes: list = boxes

        # self parent for DSU
        for box in self.boxes:
            box.parent = box

    def find(self, box):
        while box.parent != box:
            box = box.parent
        return box

    def process(self):
        pairs = []
        for i, box in enumerate(self.boxes):
            for k, other in enumerate(self.boxes):
                if i < k or box == other:
                    continue
                distance = other.distance_squared(box)
                pairs.append((distance, box, other))

        pairs = sorted(pairs, key=lambda p: p[0])

        lastconn = None
        for i, pair in enumerate(pairs):
            distance, box, other = pair
            conn = self.connect(box, other)
            if conn:
                lastconn = conn

        if lastconn:
            print(f"Last connection: {lastconn}")
            print(int(lastconn[0].x * lastconn[1].x))

    def connect(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)

        # both in circuits already
        if roota == rootb:
            return

        # merge circuits
        rootb.parent = roota
        return (a, b)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    boxes = []
    for l in lines:
        c = l.split(",")
        boxes.append(Box(float(c[0]), float(c[1]), float(c[2])))

    day8 = Day8(boxes)
    day8.process()
