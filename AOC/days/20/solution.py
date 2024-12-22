from pathlib import Path
from queue import PriorityQueue

Queue = PriorityQueue

TEST = True
TEST = False

data = open(Path(Path(__file__).parent, "test" if TEST else "input"), "r").readlines()

walls = set()

minx = miny = 1
maxx = len(data[0]) - 2
maxy = len(data) - 2

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def move(pos, direction):
    return pos[0] + direction[0], pos[1] + direction[1]


def is_valid(pos):
    return minx <= pos[0] <= maxx and miny <= pos[1] <= maxy


def is_surrounded(pos):
    for direction in directions:
        new_pos = move(pos, direction)
        if new_pos not in walls:
            return False
    return True


for y, val in enumerate(data):
    for x, char in enumerate(val):
        if char == "#":
            walls.add((x, y))
        if char == "S":
            start = (x, y)
        if char == "E":
            end = (x, y)


def bfs(walls, baseline=None):
    visited = set()
    q = Queue()
    q.put((0, start))
    visited.add(start)
    while not q.empty():
        pico, pos = q.get()
        for direction in directions:
            new_pos = move(pos, direction)
            if new_pos == end:
                return pico + 1
            if is_valid(new_pos) and new_pos not in walls and new_pos not in visited:
                visited.add(new_pos)
                if baseline:
                    if (pico + 1) > (baseline - 100):
                        continue
                q.put((pico + 1, new_pos))


if __name__ == "__main__":
    baseline = bfs(walls)
    savings = []
    for idx, wall in enumerate(walls):
        if is_surrounded(wall):
            continue
        if not is_valid(wall):
            continue
        print(f"{idx} / {len(walls)}")
        these_walls = walls.copy()
        these_walls.remove(wall)
        if (a:=bfs(these_walls, baseline)):
            savings.append(baseline - a)
    print(sum([bool(saving) for saving in savings if saving >= 100]))
