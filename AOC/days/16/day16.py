from pathlib import Path
from queue import PriorityQueue

day = 16

data = [
    list(line.strip())
    for line in open(Path(Path(__file__).parent, f"day{day}input"), "r").readlines()
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
q.put((0, start, 1))

memo = {}

if __name__ == "__main__":
    while q.not_empty:
        score, pos, direction = q.get()
        if pos in memo and memo[pos][0] == direction and memo[pos][1] <= score:
            continue
        memo[pos] = (direction, score)
        if pos == end:
            print(score)
            break

        q.put((score + 1000, pos, turn_right(direction)))
        q.put((score + 1000, pos, turn_left(direction)))
        forward = (
            score + 1,
            (pos[0] + directions[direction][0], pos[1] + directions[direction][1]),
            direction,
        )
        if grid[forward[1]] != "#":
            q.put(forward)
