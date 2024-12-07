from pathlib import Path

day = 8
test = 0

data = [line.strip()
    for line in open(Path(Path(__file__).parent, f"day{day}input"), "r").readlines()
]


if __name__ == "__main__":
    ...