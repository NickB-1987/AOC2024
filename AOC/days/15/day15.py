from pathlib import Path
import re
import time

day = 15
test = 0


grid, moves = (
    open(Path(Path(__file__).parent, f"day{day}input"), "r").read().split("\n\n")
)

moves = moves.replace("\n", "")
grid = [list(line) for line in grid.split("\n")]

directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

walls = []
boxes = []

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == "#":
            walls.append((x, y))
        elif cell == "@":
            robot = (x, y)
        elif cell == "O":
            boxes.append((x, y))


if __name__ == "__main__":
    for move in moves:
        mx, my = directions[move]
        last = robot
        these_boxes = []
        # get the boxes which are in front of the robot
        while (a := (last[0] + mx, last[1] + my)) in boxes:
            boxes.remove(a)
            these_boxes.append(a)
            last = a
        # check if there is a wall in front of the robot / after the last box
        if (last[0] + mx, last[1] + my) not in walls:
            # move the robot
            robot = (robot[0] + mx, robot[1] + my)
            # move the boxes
            for box in these_boxes:
                boxes.append((box[0] + mx, box[1] + my))
        else:
            # put the boxes back
            boxes.extend(these_boxes)
    # score is sum of 100y+x
    print("Part1: ", sum([100 * y + x for x, y in boxes]))
