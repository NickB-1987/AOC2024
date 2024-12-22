from pathlib import Path
from queue import Queue
from multiprocessing import Pool

TEST = True
# TEST = False

data = open(
            Path(Path(__file__).parent, "test" if TEST else "input"), "r"
        ).readlines()

towels = data[0].strip().split(", ")

patterns = [line.strip() for line in data[2:]]

if TEST:
    ...

def can_be_made(pattern):
    ways = 0
    memo = set()
    queue = Queue()
    queue.put(pattern)
    while not queue.empty():
        current = queue.get()
        if current == "":
            ways += 1
        for towel in towels:
            if current.startswith(towel) and current[len(towel):] not in memo:
                memo.add(current[len(towel):])
                queue.put(current[len(towel):])
    with open(Path(Path(__file__).parent, f"patterns/{pattern}"), "w") as f:
        f.write(f"{ways}")
    return ways

if __name__ == "__main__":
    p = Pool()
    success = 0
    success2 = 0
    j = len(patterns)
    ans = p.map(can_be_made, patterns)
    # for i, pattern in enumerate(patterns):
    #     ans = can_be_made(pattern, towels)
    #     print(f"Pattern {i} / {j}")
    #     success += bool(ans)
    #     success2 += ans
    success = sum([bool(a) for a in ans])
    success2 = sum(ans)
    print("Part1: ", success)
    print("Part2: ", success2)