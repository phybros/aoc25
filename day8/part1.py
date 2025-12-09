# so i can have a reference to Vec3 inside Vec3
from __future__ import annotations
from array import array
import math


class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # dropping the sqrt when we only care about the relative distances
    # makes things a bit faster
    def distance_squared(self, other: Vec3) -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return dx * dx + dy * dy + dz * dz

    def distance_to(self, other: Vec3) -> float:
        return math.sqrt(self.distance_squared(other))

    def __repr__(self):
        return f"Vec3({self.x!r}, {self.y!r}, {self.z!r})"


class Day8:
    def __init__(self, boxes: list):
        self.boxes: list = boxes
        self.circuits = []

    def get_circuit_by_box(self, box):
        for circuit in self.circuits:
            if box in circuit:
                return circuit

        return None

    def process(self):
        pairs = []
        for i, box in enumerate(self.boxes):
            for k, other in enumerate(self.boxes):
                if i < k or box == other:
                    continue
                distance = other.distance_squared(box)
                pairs.append((distance, box, other))
        pairs = sorted(pairs, key=lambda p: p[0])

        for i, pair in enumerate(pairs):
            if i >= 1000:
                break
            distance, box, other = pair
            self.connect(box, other)

        self.circuits = sorted(self.circuits, key=lambda c: len(c))

    def connect(self, a, b):
        circuita = self.get_circuit_by_box(a)
        circuitb = self.get_circuit_by_box(b)

        if circuita is None:
            if circuitb is None:
                # both None
                self.circuits.append([a, b])
            else:
                circuitb.append(a)
        else:
            if circuitb is None:
                circuita.append(b)
            else:
                # both in circuits already
                if circuita == circuitb:
                    return
                else:
                    # merge circuits
                    circuita += circuitb
                    self.circuits.remove(circuitb)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    boxes = []
    for l in lines:
        c = l.split(",")
        boxes.append(Vec3(float(c[0]), float(c[1]), float(c[2])))

    day8 = Day8(boxes)
    day8.process()

    result = 1
    for c in day8.circuits[-3:]:
        result *= len(c)

    print(result)
