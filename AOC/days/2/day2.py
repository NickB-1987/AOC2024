from pathlib import Path

day = 2

expected_test_result = 2

data = [
    [int(x) for x in y]
    for y in [
        line.strip().split(" ")
        for line in open(Path(Path(__file__).parent, f"day{day}input"), "r").readlines()
    ]
]


def is_line_safe(line: list[int]) -> bool:
    safe = True
    for i in range(len(line) - 1):
        diff = line[i + 1] - line[i]
        if diff == 0:
            safe = False
        elif i == 0:
            sign = diff / abs(diff)
        if (abs(diff) > 3) or (abs(diff) < 1) and safe:
            safe = False
        if safe and diff / abs(diff) != sign:
            safe = False
    return safe


def check(data: list[list[int]]):
    unsafe_lines: list[list[int]] = []
    safes = 0
    for line in data:
        safe = is_line_safe(line)
        if safe:
            safes += 1
        else:
            unsafe_lines.append(line)
    print("Pt1: ", safes)
    for line in unsafe_lines:
        for i in range(len(line)):
            _line = line.copy()
            del _line[i]
            safe = is_line_safe(_line)
            if safe:
                safes += 1
                break
    print("pt2: ", safes)


if __name__ == "__main__":
    check(data)
