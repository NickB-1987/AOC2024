from pathlib import Path
import re
import time

day = 14
test = 0
# p=0,4 v=3,-3
match = re.compile(r"p=([-+]?\d+)\,([-+]?\d+) v=([-+]?\d+)\,([-+]?\d+)")

data = open(Path(Path(__file__).parent, f"day{day}input"), "r").read()

matches = re.findall(match, data)

start_robots = []

for match in matches:
    # robots are px, py, vx, vy
    start_robots.append(tuple(int(x) for x in match))

grid_x = 101
grid_y = 103


if __name__ == "__main__":
    seconds = 100
    end_robots = {"tl": [], "tr": [], "bl": [], "br": []}
    mid_x = grid_x // 2
    mid_y = grid_y // 2
    for robot in start_robots:
        robot_end = (
            (robot[0] + (robot[2] * seconds)) % grid_x,
            (robot[1] + (robot[3] * seconds)) % grid_y,
        )
        if robot_end[0] < mid_x:
            if robot_end[1] < mid_y:
                end_robots["tl"].append(robot_end)
            elif robot_end[1] > mid_y:
                end_robots["bl"].append(robot_end)
        elif robot_end[0] > mid_x:
            if robot_end[1] < mid_y:
                end_robots["tr"].append(robot_end)
            elif robot_end[1] > mid_y:
                end_robots["br"].append(robot_end)
    a = 1
    for val in end_robots.values():
        a *= len(val)
    print("Part 1: ", a)

    results = {}
    end_robots = []
    for seconds in range(10000):
        end_robots = []
        for robot in start_robots:
            end_robots.append(
                (
                    (robot[0] + (robot[2] * seconds)) % grid_x,
                    (robot[1] + (robot[3] * seconds)) % grid_y,
                )
            )

        x_s = [x[0] for x in end_robots]
        y_s = [x[1] for x in end_robots]
        xmean = sum(x_s) / len(x_s)
        ymean = sum(y_s) / len(y_s)
        x_var = sum((x - xmean) ** 2 for x in x_s) / len(x_s)
        y_var = sum((y - ymean) ** 2 for y in y_s) / len(y_s)
        results[seconds] = (x_var, y_var)
        if x_var < 600 and y_var < 600:
            print("Part 2: ", seconds)
            pr = True
        else:
            pr = False
        if pr:
            for y in range(grid_y):
                row = ""
                for x in range(grid_x):
                    if (x, y) in end_robots:
                        row += "#"
                    else:
                        row += "."
                print(row)
            break
