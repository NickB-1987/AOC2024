from pathlib import Path
import re
from scipy.optimize import linprog

day = 13
test = 0

match = re.compile(
    r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
)

data = open(Path(Path(__file__).parent, f"day{day}input"), "r").read()

matches = re.findall(match, data)

machines = []

for match in matches:
    ax, ay, bx, by, px, py = (int(x) for x in match)
    machines.append((ax, ay, bx, by, px, py))


if __name__ == "__main__":

    for mod in [0, 10000000000000]:
        cost = 0
        for machine in machines:
            obj = [3, 1]
            lhs_eq = [[machine[0], machine[2]], [machine[1], machine[3]]]
            rhs_eq = [machine[4] + mod, machine[5] + mod]
            opt = linprog(
                c=obj,
                A_eq=lhs_eq,
                b_eq=rhs_eq,
                bounds=[(0, None), (0, None)],
                integrality=1,
                method="highs",
                options={"presolve": False},
            )
            if opt.success:
                cost += opt.fun
        print(cost)
