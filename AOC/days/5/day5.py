from pathlib import Path
from itertools import permutations
from functools import cmp_to_key

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

    def cust_sort(a, b):
        for rule in rules:
            if rule[0] in [a, b] and rule[1] in [a, b]:
                if a == rule[0]:
                    return -1
                else:
                    return 1

    for line in badlines:
        while not is_good(line):
            line.sort(key=cmp_to_key(cust_sort))
        new_goodlines.append(line)

    print("Part2: ", sum([line[len(line) // 2] for line in new_goodlines]))
