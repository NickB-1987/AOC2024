from pathlib import Path
import re
day = 3

expected_test_result = 161

data = open(Path(Path(__file__).parent, f"day{day}test"), "r").read()

# match = re.compile(r'mul\(\d{1,},\d{1,}\)')
match = re.compile(r'mul\(\d{1,},\d{1,}\)|do\(\)|don\'t\(\)')

if __name__ == "__main__":
    total = 0
    matches = re.findall(match, data)
    do = True
    for match in matches:
        if match == 'do()':
            do = True
        elif match == "don't()":
            do = False
        else:
            if do:
                nums = [int(x) for x in match.replace("mul(", "").replace(")", "").split(",")]
                total += nums[0] * nums[1]
    print(total)

    