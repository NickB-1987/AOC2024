from pathlib import Path

day = 7
test = 0

data = [
    [int(line[0]), [int(num) for num in line[1].strip().split(" ")]]
    for line in [
        line.strip().split(":")
        for line in open(Path(Path(__file__).parent, f"day{day}input"), "r").readlines()
    ]
]


if __name__ == "__main__":
    total = 0
    vals = []
    for ans, _nums in data:
        nums = _nums.copy()
        vals = []
        vals.append(nums.pop(0))
        while len(nums) > 0:
            modifier = nums.pop(0)
            vals = [val * modifier for val in vals] + [val + modifier for val in vals]
        if ans in vals:
            total += ans
    print("Part 1: ", total)

    # Part 2
    vals = []
    total = 0
    for ans, _nums in data:
        nums = _nums.copy()
        vals = []
        vals.append(nums.pop(0))
        while len(nums) > 0:
            modifier = nums.pop(0)
            vals = (
                [val * modifier for val in vals]
                + [val + modifier for val in vals]
                + [int(f"{val}{modifier}") for val in vals]
            )
        if ans in vals:
            total += ans
    print("Part 2: ", total)
