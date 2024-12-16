from pathlib import Path

day = 16


data = [list(line.strip()) for line in open(Path(Path(__file__).parent, f"day{day}test"), "r").readlines()]

max_y = len(data)
max_x = len(data[0])

grid: dict[tuple[int, int], str] = {}

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == 'S':
            start = (x, y)
        elif char == 'E':
            end = (x, y)
        else:
            grid[(x, y)] = char


if __name__ == "__main__":
    ...