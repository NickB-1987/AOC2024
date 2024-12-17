from pathlib import Path
from queue import PriorityQueue

day = 16

data = [
    list(line.strip())
    for line in open(Path(Path(__file__).parent, f"day{day}test2"), "r").readlines()
]

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

grid: dict[tuple[int, int], str] = {}

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == "S":
            start = (x, y)
            grid[(x, y)] = "."
        elif char == "E":
            end = (x, y)
            grid[(x, y)] = "."
        else:
            grid[(x, y)] = char


def turn_left(d):
    return (d - 1) % 4


def turn_right(d):
    return (d + 1) % 4


q = PriorityQueue()

# store steps as (score, (x, y), direction)
# forward = 1 point
# right or left = 1000 points
q.put((0, start, 1, set()))

memo = {}

if __name__ == "__main__":
    results = []
    target_score = 0

    finish = False

    while q.not_empty and not finish:
        score, pos, direction, path = q.get()
        # if pos in memo and memo[pos][0] == direction and memo[pos][1] <= score:
        #     continue
        # memo[pos] = (direction, score)

        if pos == end:
            if not results:
                target_score = score
                print(score)
                results.append(path)
            if score == target_score:
                results.append(path)
            if score > target_score:
                finish = True

        path.add(pos)

        q.put((score + 1000, pos, turn_right(direction), path.copy()))
        q.put((score + 1000, pos, turn_left(direction), path.copy()))
        forward = (
            score + 1,
            (pos[0] + directions[direction][0], pos[1] + directions[direction][1]),
            direction,
            path.copy(),
        )
        if grid[forward[1]] != "#":
            q.put(forward)
    myset = set()
    for i in results:
        myset = myset.union(i)
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if (x, y) in myset:
                print("O", end="")
            else:
                print(char, end="")
        print()
    print(len(myset))
