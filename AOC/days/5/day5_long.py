from pathlib import Path
from itertools import permutations
from multiprocessing import Pool

day = 5

expected_test_result = 11

data = [
    line.strip()
    for line in open(Path(Path(__file__).parent, f"day{day}input"), "r").readlines()
]

rules = [
    [int(x) for x in y]
    for y in [line.split("|") for line in data if line != "" and "|" in line]
]
printlines = [
    [int(x) for x in y]
    for y in [line.split(",") for line in data if "|" not in line and line != ""]
]


def is_good(line):
    good = True
    for rule in rules:
        try:
            idx1 = line.index(rule[0])
            idx2 = line.index(rule[1])
        except ValueError:
            idx1 = 0
            idx2 = 0
            pass
        if idx1 > idx2:
            good = False
    return good


def check_perms(line):
    for perm in permutations(line):
        if is_good(perm):
            return perm


if __name__ == "__main__":
    goodlines = []
    badlines = []
    for line in printlines:
        if is_good(line):
            goodlines.append(line)
        else:
            badlines.append(line)
    print("Part1: ", sum([line[len(line) // 2] for line in goodlines]))

    # Part 2
    new_goodlines = []

    p = Pool()
    new_goodlines = p.map(check_perms, badlines)

    print("Part2: ", sum([line[len(line) // 2] for line in new_goodlines]))
