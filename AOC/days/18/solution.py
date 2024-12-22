from pathlib import Path
from queue import Queue

TEST = True
TEST = False

data = [
    (int(x), int(y))
    for x, y in [
        line.strip().split(",")
        for line in open(
            Path(Path(__file__).parent, "test" if TEST else "input"), "r"
        ).readlines()
    ]
]

x_lim = 70
y_lim = 70
bytes_to_fall = 1024
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def oob(x, y):
    return x < 0 or x > x_lim or y < 0 or y > y_lim


def move(coord, direction):
    return (coord[0] + direction[0], coord[1] + direction[1])


if TEST:
    x_lim = 6
    y_lim = 6
    bytes_to_fall = 12

start = (0, 0)
end = (x_lim, y_lim)


if __name__ == "__main__":
    corrupted = {data[i] for i in range(bytes_to_fall)}

    q = Queue()
    visited = set()
    visited.add(start)
    q.put((0, start))
    while not q.empty():
        steps, pos = q.get()
        new_steps = steps + 1
        for direction in directions:
            new_pos = move(pos, direction)
            if new_pos == end:
                print("Part 1: ", new_steps)
                break
            if oob(*new_pos) or new_pos in visited or new_pos in corrupted:
                continue
            q.put((new_steps, new_pos))
            visited.add(new_pos)
        if new_pos == end:
            break

    for byte in data[bytes_to_fall:]:
        corrupted.add(byte)
        q = Queue()
        visited = set()
        visited.add(start)
        q.put((0, start))
        while not q.empty():
            steps, pos = q.get()
            new_steps = steps + 1
            for direction in directions:
                new_pos = move(pos, direction)
                if new_pos == end:
                    break
                if oob(*new_pos) or new_pos in corrupted or new_pos in visited:
                    continue
                q.put((new_steps, new_pos))
                visited.add(new_pos)
            if new_pos == end:
                break
        if new_pos != end:
            print("Part 2: ", ",".join([str(i) for i in byte]))
            break
