from pathlib import Path
from collections import defaultdict

TEST = True
TEST = False

pairs = [
    line.strip().split("-")
    for line in open(
        Path(Path(__file__).parent, "test" if TEST else "input"), "r"
    ).readlines()
]

computers = defaultdict(set)

for pair in pairs:
    a, b = pair
    computers[a].add(b)
    computers[b].add(a)

if __name__ == "__main__":
    groups = set()
    for x in computers:
        for y in computers[x]:
            for z in computers[y]:
                if x in computers[z]:
                    if any(a.startswith("t") for a in [x, y, z]):
                        groups.add(tuple(sorted([x, y, z])))
    print("Part 1: ", len(groups))

    groups = set()
    for x in computers:
        party = set([x])
        for y in computers:
            if all(z in computers[y] for z in party):
                party.add(y)
        groups.add(tuple(sorted(party)))
    biggest_party = max(groups, key=len)
    print("Part 2: ", ",".join(biggest_party))
