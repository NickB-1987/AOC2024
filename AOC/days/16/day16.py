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

q = PriorityQueue()

q.put((0, start, 1, [start]))

memo = set()

if __name__ == "__main__":
    results = set()
    target_score = 10000000

    finish = False

    while q.not_empty and not finish:
        score, pos, direction, path = q.get()
        memo.add((pos, direction))
        if score > target_score:
            finish = True
        if pos == end:
            if len(results) == 0:
                target_score = score
                print("Part 1: ", score)
                results.update(path)
            if score == target_score:
                results.update(path)

        for d in [0, -1, 1]:
            new_dir = (direction + d) % 4
            dir = directions[new_dir]
            new_score = score + (abs(d) * 1000) + 1
            new_pos = (pos[0] + directions[new_dir][0], pos[1] + directions[new_dir][1])
            new_path = path + [new_pos]
            if (new_pos, new_dir) in memo:
                continue
            if grid[new_pos] != "#":
                q.put((score + (abs(d) * 1000) + 1, new_pos, new_dir, new_path))

    print("Part 2: ", len(results))
