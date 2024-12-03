from pathlib import Path
day = 1

expected_test_result = 11

data = [line.strip().split("   ") for line in open(Path(Path(__file__).parent, f"day{day}input"), "r").readlines()]

if __name__ == "__main__":

    print(sum([abs(a - b) for a, b in list(zip(sorted([int(x[0]) for x in data]), sorted([int(x[1]) for x in data])))]))

    print(sum([number * len([x for x in [int(x[1]) for x in data] if x == number]) for number in [int(x[0]) for x in data]]))

