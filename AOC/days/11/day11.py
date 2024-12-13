from pathlib import Path

day = 11
test = 0

data = [
    int(x)
    for x in open(Path(Path(__file__).parent, f"day{day}input"), "r")
    .readline()
    .split(" ")
]

BLINKS = 75

memo = {}


def score(num, blinks):
    # print(blinks)
    if blinks == BLINKS:
        return 1
    if (num, blinks) in memo:
        blinks += 1
        return memo[(num, blinks - 1)]
    if num == 0:
        memo[(num, blinks)] = score(1, blinks + 1)
    elif ((b := len(a := str(num))) % 2) == 0:
        memo[(num, blinks)] = score(int(a[: b // 2]), blinks + 1) + score(
            int(a[b // 2 :]), blinks + 1
        )
    else:
        memo[(num, blinks)] = score(2024 * num, blinks + 1)
    return score(num, blinks)


if __name__ == "__main__":

    s = 0
    for number in data:
        s += score(number, 0)
    print(s)
