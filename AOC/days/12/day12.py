from pathlib import Path
from queue import Queue

day = 12
test = 0


data = [
    list(line.strip())
    for line in open(Path(Path(__file__).parent, f"day{day}input"), "r").readlines()
]

maxy = len(data) - 1
maxx = len(data[0]) - 1
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_neighbour(letter: str, coord: tuple[int], direction: tuple[int]) -> bool:
    new = (coord[0] + direction[0], coord[1] + direction[1])
    if (new[0] < 0) or (new[0] > maxx) or (new[1] < 0) or (new[1] > maxy):
        return False
    if data[new[1]][new[0]] == letter:
        return True
    else:
        return False


def find_region(letter: str, coord: tuple[int]):
    squares = set()
    squares.add(coord)
    q = Queue()
    q.put(coord)
    edges = 0
    while not q.empty():
        square = q.get()
        for direction in directions:
            if is_neighbour(letter, square, direction):
                new = (square[0] + direction[0], square[1] + direction[1])
                if new not in squares:
                    q.put(new)
                squares.add(new)
            else:
                edges += 1
    return squares, edges


if __name__ == "__main__":
    price = 0
    already_found = set()
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            if (x, y) not in already_found:
                letter = data[y][x]
                region, edges = find_region(letter, (x, y))
                already_found = already_found.union(region)
                this_price = len(region) * edges
                price += this_price
    print(price)