from pathlib import Path
import operator

TEST = True
TEST = False

data = [
    line.strip()
    for line in open(
        Path(Path(__file__).parent, "test2" if TEST else "input"), "r"
    ).readlines()
]

known_wires = {}
gates = []

for line in data:
    if ":" in line:
        a, b = line.split(": ")
        known_wires[a] = b
    elif line == "":
        continue
    else:
        gate = line.split(" ")
        if gate[4] not in known_wires:
            gates.append(gate)

ops = {"AND": operator.and_, "OR": operator.or_, "XOR": operator.xor}

if __name__ == "__main__":
    while gates:
        for gate in gates:
            if (
                gate[0] in known_wires
                and gate[2] in known_wires
                and gate[4] not in known_wires
            ):
                known_wires[gate[4]] = str(
                    ops[gate[1]](int(known_wires[gate[0]]), int(known_wires[gate[2]]))
                )
                gates.remove(gate)
    z_s = dict(
        sorted(
            {k: v for k, v in known_wires.items() if k.startswith("z")}.items(),
            reverse=True,
        )
    )
    print("Part 1: ", int("".join(z_s.values()), 2))
