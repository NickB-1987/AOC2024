from pathlib import Path
day = 4

expected_test_result = 11

data = [line.strip().split("") for line in open(Path(Path(__file__).parent, f"day{day}input"), "r").readlines()]

if __name__ == "__main__":
    ...