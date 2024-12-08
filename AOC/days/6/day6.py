from copy import deepcopy
from pathlib import Path

day = 6
test = 41

_data = [
    list(line.strip())
    for line in open(Path(Path(__file__).parent, f"day{day}input"), "r").readlines()
]

data = deepcopy(_data)

max_x = len(data[0])
max_y = len(data)

for y in range(max_y - 1):
    for x in range(max_x - 1):
        if data[y][x] == "^":
            starting_point = (x, y)
            data[y][x] = "X"

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

if __name__ == "__main__":
    direction = 0

    current_position = starting_point

    positions_visited = 0

    X_s: set[tuple[int]] = set()

    while True:
        d = directions[direction]
        next_pos = (current_position[0] + d[0], current_position[1] + d[1])
        if (
            (next_pos[0] < 0)
            or (next_pos[0] >= max_x)
            or (next_pos[1] < 0)
            or (next_pos[1] >= max_y)
        ):
            positions_visited += 1
            break
        c = data[next_pos[1]][next_pos[0]]
        if c == ".":
            X_s.add(next_pos)
            current_position = next_pos
            positions_visited += 1
            data[next_pos[1]][next_pos[0]] = "X"
        elif c == "X":
            current_position = next_pos
        elif c == "#":
            direction = (direction + 1) % 4
        else:
            print(c)
    print("Part 1: ", positions_visited)

    # Part 2
    valid_obstacles = 0
    data = deepcopy(_data)
    for X in X_s:
        data[X[1]][X[0]] = "X"
    # Try dropping an obsactle on each X and see if it goes back to starting pos
    i = 0
    for X in X_s:
        print(i, " / ", len(X_s))
        i += 1
        positions_visited_and_directions: list[
            tuple[int]
        ] = []  # in the format (x, y, d)
        direction = 0
        # da = deepcopy(data)
        da = data
        da[X[1]][X[0]] = "#"
        current_position = starting_point
        while True:
            d = directions[direction]
            next_pos = (current_position[0] + d[0], current_position[1] + d[1])
            if (
                (next_pos[0] < 0)
                or (next_pos[0] >= max_x)
                or (next_pos[1] < 0)
                or (next_pos[1] >= max_y)
            ):
                da[X[1]][X[0]] = "X"
                break
            this_pos_and_d = (next_pos[0], next_pos[1], direction)
            if this_pos_and_d in positions_visited_and_directions:
                valid_obstacles += 1
                da[X[1]][X[0]] = "X"
                break
            positions_visited_and_directions.append(this_pos_and_d)
            c = da[next_pos[1]][next_pos[0]]
            if c == "#":
                direction = (direction + 1) % 4
                continue
            current_position = next_pos
    print("Part 2: ", valid_obstacles)
