from pathlib import Path
from queue import Queue

day = 10
test = 0

data = [[int(x) for x in list(line.strip())] for line in open(Path(Path(__file__).parent, f"day{day}test"), "r").readlines()]

maxy = len(data) - 1
maxx = len(data[0]) - 1

coords = set()

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
                coords.add((x, y))
    i = 1
    while i < 10:
        new_coords = set()
        :
            coord = coords.pop()
            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if not coord_oob(coord, direction):
                    new = move(coord, direction)
                    if data[new[1]][new[0]] == i:
                        new_coords.add(new)
        coords = new_coords
        i += 1
        print(len(new_coords))




            

