from pathlib import Path

TEST = True
# TEST = False

data = open(Path(Path(__file__).parent, "test" if TEST else "input"), "r").readlines()

if __name__ == "__main__":
    ...
