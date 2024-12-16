from pathlib import Path
from heapq import heappush, heappop

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
        elif char == "E":
            end = (x, y)
        else:
            grid[(x, y)] = char

def turn_left(d):
    return (d - 1) % 4
def turn_right(d):
    return (d + 1) % 4

q = []

# store steps as (score, (x, y), direction)
# forward = 1 point
# right or left = 1000 points

heappush(q, (0, start, 1))

memo = {}

if __name__ == "__main__":
    while q:
        # print(len(q))
        score, pos, direction = heappop(q)
        if pos in memo and memo[pos][0] == direction and memo[pos][1] <= score:
            continue
        if pos == end:
            print(score)
            break

        right = (score + 1000, pos, turn_right(direction))
        left = (score + 1000, pos, turn_left(direction))
        forward = (score + 1, (pos[0] + directions[direction][0], pos[1] + directions[direction][1]), direction)
        if grid.get(forward[1], None) != "#":
            heappush(q, forward)
        heappush(q, right)
        heappush(q, left)

