class Machine:

    def __init__(self, onlights, buttons, onjoltage):
        self.lights = ["." for i in range(len(onlights))]
        self.onlights = onlights
        self.buttons = buttons
        self.joltage = [0 for i in range(len(onjoltage))]
        self.onjoltage = onjoltage
    
    def toggle_lights(self, pattern):
        if len(self.lights) != len(pattern):
            print("pattern length isn't right")
            return

        for i in range(len(self.lights)):
            if pattern[i] == '.':
                continue
            else:
                self.lights[i] = '#' if self.lights[i] == '.' else '.'

    def reset(self):
        self.lights = ["." for i in range(len(self.onlights))]
        self.joltage = [0 for i in range(len(self.onjoltage))]

    def increment_joltage(self, pattern):
        if len(self.joltage) != len(pattern):
            print("pattern length isn't right")
            return

        for i in range(len(self.joltage)):
            if pattern[i] == '.':
                continue
            else:
                self.joltage[i] += 1

class MachineHelper:

    @staticmethod
    def machinelist(filename):
        machines = []

        with open(filename, "r") as f:
            for line in f.readlines():
                line = line.strip()

                lights, rest = line.split(" ", 1)
                buttons, joltage = rest.rsplit(" ", 1)

                machineonlights = list(lights.strip("[]"))
                machinebuttons = []
                for w in buttons.split(" "):
                    w = w.strip("()")
                    ls = w.split(",")

                    button = "." * len(machineonlights)
                    for l in ls:
                        lint = int(l)
                        bs = list(button)
                        bs[lint] = "#"
                        button = "".join(bs)                    

                    machinebuttons.append(list(button))

                joltage = joltage.strip("}{")
                onjoltage = [int(x) for x in joltage.split(",")]

                machines.append(Machine(machineonlights, machinebuttons, onjoltage))
        
        return machines