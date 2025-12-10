from machine import MachineHelper
import pulp

# is this cheating? use PuLP to solve this
def find_min_presses(machine):
    numpositions = len(machine.onjoltage)
    numbuttons = len(machine.buttons)

    prob = pulp.LpProblem("part2", pulp.LpMinimize)

    buttonpresses = []

    for i in range(numbuttons):
        p = pulp.LpVariable(f"button{i}", lowBound=0, cat='Integer')
        buttonpresses.append(p)

    prob += pulp.lpSum(buttonpresses)

    for i in range(numpositions):
        increment = pulp.lpSum(
            buttonpresses[j] if machine.buttons[j][i] == '#' else 0
            for j in range(numbuttons)
        )
        prob += increment == machine.onjoltage[i], f"position{i}"

    # actually solve the thing
    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    if prob.status == pulp.LpStatusOptimal:
        return int(pulp.value(prob.objective))
    else:
        return -1


if __name__ == "__main__":
    machines = MachineHelper.machinelist("input.txt")

    total = 0
    for m, machine in enumerate(machines):
        minpresses = find_min_presses(machine)
        print(f"Machine {m+1}: {minpresses} presses")
        total += minpresses

    print(f"Total: {total}")
