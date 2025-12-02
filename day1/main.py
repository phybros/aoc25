import re
import math

ROTATION_PATTERN = "([LR])(\\d+)"

# the thing says "The dial starts by pointing at 50."
current = 50
zeroes = 0
passed_zeroes = 0

with open("input.txt", "r") as f:
    # be fancy and use a list comprehension
    rotations = [r.strip() for r in f.read().split("\n") if r.strip() != ""]

# just for testing
stopafter = 99999

for rotation in rotations:
    if stopafter <= 0:
        break

    stopafter -= 1
    matches = re.match(ROTATION_PATTERN, rotation)
    m = matches.groups()

    # turn L into -1 and R into 1
    direction = -1 if m[0] == "L" else 1
    distance = int(m[1])

    # the amount we will move
    move = distance * direction

    # old is just for printing
    old = current

    if abs(move) >= 100:
        # since we aren't actually opening the safe, just throw everyhing away except the remainder lol
        remainder = abs(move) % 100

        full_rotations = math.floor(abs(move) / 100)
        passed_zeroes += full_rotations

        current += remainder * direction
    else:
        current += move

    # handle wrapping around because there are 100 numbers in a circle:
    # "Because the dial is a circle, turning the dial left from 0 one click makes it point at 99."
    # "Similarly, turning the dial right from 99 one click makes it point at 0."
    #
    # also going from or to 0 doesn't count as passing zero when we're doing wrapping
    if current > 99:
        current -= 100
        if old != 0 and current != 0:
            passed_zeroes += 1
    elif current < 0:
        current += 100
        if old != 0 and current != 0:
            passed_zeroes += 1

    if current == 0:
        zeroes += 1

print(f"Total Zeroes Stoped On: {zeroes}")
print(f"Total Passed Zeroes: {passed_zeroes}")
print(f"Total: {zeroes + passed_zeroes}")
