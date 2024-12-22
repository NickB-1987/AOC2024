from pathlib import Path
from collections import defaultdict


TEST = True
TEST = False

data = [
    int(x)
    for x in open(
        Path(Path(__file__).parent, "test2" if TEST else "input"), "r"
    ).readlines()
]
buyers = data


def generate_next(num: int) -> int:
    num ^= num * 64
    num = num % 16777216
    num ^= num // 32
    num = num % 16777216
    num ^= num * 2048
    num = num % 16777216
    return num


if __name__ == "__main__":
    # Part 1
    nums = 0
    buyer_nums: dict[tuple[int, int], list[int]] = {
        (idx, buyer): [buyer % 10] for idx, buyer in enumerate(buyers)
    }
    for idx, buyer in enumerate(buyers):
        num = buyer
        for _ in range(2000):
            num = generate_next(num)
            buyer_nums[(idx, buyer)].append(num % 10)
        nums += num
    print("Part 1: ", nums)

    # Part 2
    all_buyers: dict[tuple[int, ...], int] = defaultdict(int)
    for buyer, nums in buyer_nums.items():
        this_buyer: dict[tuple[int, ...], int] = defaultdict(int)
        diffs = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
        for i in range(4, len(nums)):
            diff_tup: tuple[int, ...] = tuple(diffs[i - 4 : i])
            if diff_tup in this_buyer:
                continue
            all_buyers[diff_tup] += nums[i]
            this_buyer[diff_tup] = nums[i]
    print("Part 2: ", max(all_buyers.values()))
