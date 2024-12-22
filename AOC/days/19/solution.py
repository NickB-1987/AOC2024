from pathlib import Path
from queue import Queue
from multiprocessing import Pool

TEST = True
TEST = False

data = open(Path(Path(__file__).parent, "test" if TEST else "input"), "r").readlines()

towels = data[0].strip().split(", ")

patterns = [line.strip() for line in data[2:]]

if TEST:
    ...

memo = dict()


def can_be_made(pattern):
    ways = 0
    memo = dict()
    queue = Queue()
    queue.put(pattern)
    while not queue.empty():
        current = queue.get()
        if current in memo:
            return memo[current]
        if current == "":
            ways += 1
        for towel in towels:
            if current.startswith(towel):
                queue.put(current[len(towel) :])
    return ways


def find_pattern(pattern: str):
    if pattern == "":
        return 1
    if pattern in memo:
        return memo[pattern]
    ways = 0
    for towel in towels:
        if pattern.startswith(towel):
            ways += find_pattern(pattern[len(towel) :])
    memo[pattern] = ways
    return ways


if __name__ == "__main__":
    ans = [find_pattern(p) for p in patterns]
    success = sum([bool(a) for a in ans])
    success2 = sum(ans)
    print("Part1: ", success)
    print("Part2: ", success2)
