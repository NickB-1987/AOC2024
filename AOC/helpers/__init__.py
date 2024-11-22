from pathlib import Path

def get_data(path: Path) -> list[str]:
    return [line.strip() for line in open(path, "r").readlines()]