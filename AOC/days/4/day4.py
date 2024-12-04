from pathlib import Path

day = 4

expected_test_result = 11

data = [
    list(line.strip())
    for line in open(Path(Path(__file__).parent, f"day{day}input"), "r").readlines()
]
y_max = len(data) - 1
x_max = len(data[0]) - 1

# list of potential coordinate modifiers for each direction of word
directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def check(
    letter: str, start_coords: tuple[int], direction: tuple[int], mult: int
) -> bool:
    x = start_coords[0] + direction[0] * mult
    y = start_coords[1] + direction[1] * mult
    if (x < 0) or (y < 0) or (y > y_max) or (x > x_max):
        return False
    if data[y][x] == letter:
        return True
    else:
        return False


if __name__ == "__main__":
    # part 1...
    xmases = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "X":
                for d in directions:
                    if (
                        check("M", (x, y), d, 1)
                        and check("A", (x, y), d, 2)
                        and check("S", (x, y), d, 3)
                    ):
                        xmases += 1
    print("Part1 :", xmases)

    # Part 2
    xmases = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "A":
                d = [(1, 1), (1, -1)]
                if (check("M", (x, y), d[0], 1) and check("S", (x, y), d[0], -1)) or (
                    check("S", (x, y), d[0], 1) and check("M", (x, y), d[0], -1)
                ):
                    if (
                        check("M", (x, y), d[1], 1) and check("S", (x, y), d[1], -1)
                    ) or (check("S", (x, y), d[1], 1) and check("M", (x, y), d[1], -1)):
                        xmases += 1

    print("Part2 :", xmases)
