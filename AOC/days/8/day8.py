from pathlib import Path
import string
from itertools import combinations

day = 8
test = 0

data = [
    list(line.strip())
    for line in open(Path(Path(__file__).parent, f"day{day}input"), "r").readlines()
]

letters = {x: [] for x in list(string.ascii_letters + string.digits)}

ymax = len(data)
xmax = len(data[0])

antinodes: set[tuple[int]] = set()


def check_coord_in_bounds(coord: tuple[int]) -> bool:
    if (coord[0] < 0) or (coord[0] >= xmax):
        return False
    if (coord[1] < 0) or (coord[1] >= ymax):
        return False
    return True


def calculate_antinodes(coords_a: tuple[int], coords_b: tuple[int]) -> list[tuple[int]]:
    y_diff = coords_a[1] - coords_b[1]
    x_diff = coords_a[0] - coords_b[0]
    antinode_a = (coords_a[0] + x_diff, coords_a[1] + y_diff)
    antinode_b = (coords_b[0] - x_diff, coords_b[1] - y_diff)
    out = []
    if check_coord_in_bounds(antinode_a):
        out.append(antinode_a)
    if check_coord_in_bounds(antinode_b):
        out.append(antinode_b)
    return out


def next_antinode(coords: tuple[int], x_diff: int, y_diff: int) -> tuple[int]:
    return (coords[0] + x_diff, coords[1] + y_diff)


def calculate_antinodes_pt2(
    coords_a: tuple[int], coords_b: tuple[int]
) -> list[tuple[int]]:
    out = [coords_a, coords_b]
    y_diff = coords_a[1] - coords_b[1]
    x_diff = coords_a[0] - coords_b[0]
    # Go out from a first
    while True:
        ant = next_antinode(coords_a, x_diff, y_diff)
        if not check_coord_in_bounds(ant):
            break
        out.append(ant)
        coords_a = ant
    # And then b
    while True:
        ant = next_antinode(coords_b, -x_diff, -y_diff)
        if not check_coord_in_bounds(ant):
            break
        out.append(ant)
        coords_b = ant
    return out


if __name__ == "__main__":
    for y in range(ymax):
        for x in range(xmax):
            if (a := data[y][x]).isalnum():
                letters[a].append((x, y))

    letters = {k: v for k, v in letters.items() if v}

    for key, val in letters.items():
        coords = combinations(val, 2)
        for coord in coords:
            for antinode in calculate_antinodes(coord[0], coord[1]):
                antinodes.add(antinode)

    print("Part 1: ", len(antinodes))

    antinodes = set()

    for key, val in letters.items():
        coords = combinations(val, 2)
        for coord in coords:
            for antinode in calculate_antinodes_pt2(coord[0], coord[1]):
                antinodes.add(antinode)

    print("Part 2: ", len(antinodes))
