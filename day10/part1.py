from itertools import combinations
from collections import defaultdict
from machine import MachineHelper

if __name__ == "__main__":
    machines = MachineHelper.machinelist("input.txt")

    total = 0
    for m, machine in enumerate(machines):
        found = False

        for i in range(1, len(machine.buttons) + 1):
            if found:
                break

            for combo in combinations(machine.buttons, i):
                machine.reset()

                for button in combo:
                    machine.toggle_lights(button)
                if machine.lights == machine.onlights:
                    found = True
                    total += i
                    break

    print(f"Total: {total}")
