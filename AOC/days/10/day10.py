from pathlib import Path
from queue import Queue

day = 10
test = 0

data = [[int(x) for x in list(line.strip())] for line in open(Path(Path(__file__).parent, f"day{day}input"), "r").readlines()]

maxy = len(data) - 1
maxx = len(data[0]) - 1

zeroes = []
scores = []

def coord_oob(coord, direction) -> bool:
    if ((coord[0] + direction[0]) > maxx or
        (coord[0] + direction[0]) < 0 or
        (coord[1] + direction[1]) > maxy or
        (coord[1] + direction[1]) < 0):
        return True
    else:
        return False

def move(coord, direction) -> tuple[int]:
    return ((coord[0] + direction[0], coord[1] + direction[1]))


if __name__ == "__main__":
    for y, line in enumerate(data):
        for x, val in enumerate(line):
            if val == 0:
                zeroes.append((x, y))
    # Part 1 - 36
    for zero in zeroes:
        score = 0
        i = 1
        coords = set()
        coords.add(zero)
        while i < 10 and len(coords) > 0:
            new_coords = set()
            coord_s = list(coords)
            for coord in coord_s:
                for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if not coord_oob(coord, direction):
                        new = move(coord, direction)
                        if data[new[1]][new[0]] == i:
                            new_coords.add(new)
            coords = new_coords
            i += 1
        scores.append(len(coords))
    print("Part 1: ",sum(scores))

    # Part 2 - 81
    rating = 0
    for zero in zeroes:
        q = Queue()
        q.put((1, zero))
        while not q.empty():
            next_target, last_coord = q.get()
            if next_target == 10:
                rating += 1
            else:
                for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if not coord_oob(last_coord, direction):
                        new = move(last_coord, direction)
                        if data[new[1]][new[0]] == next_target:
                            q.put((next_target + 1, new))
    print(rating)


