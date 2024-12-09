from pathlib import Path
from copy import deepcopy

day = 9
test = 0

data = open(Path(Path(__file__).parent, f"day{day}input"), "r").readline().strip()

files_free_space = []

if __name__ == "__main__":
    for idx, character in enumerate(data):
        if idx % 2 == 0:
            files_free_space += list([str(int(idx / 2))] * int(character))
        else:
            files_free_space += list("." * int(character))
    checksum = 0
    ffs = deepcopy(files_free_space)
    def calc_checksum(files_free_space):
        checksum = 0
        for idx, val in enumerate(files_free_space):
            if val == '.':
                while files_free_space[-1] == '.':
                    files_free_space.pop(-1)
                try:
                    files_free_space[idx] = files_free_space.pop(-1)
                except IndexError:
                    pass
            try:
                checksum += idx * (int(files_free_space[idx]))
            except IndexError:
                pass
        return checksum
    part1 = calc_checksum(files_free_space)
    print("part 1: ", part1)

    # Part 2
    length = len(ffs)
    ignore = ['.']
    end_cursor = length - 1
    while ffs[end_cursor] in ignore:
        end_cursor -= 1
    character = ffs[end_cursor]
    while (-end_cursor) < length:
        # Find and count the next character to move left
        while ((ffs[end_cursor] in ignore) or (int(ffs[end_cursor]) > int(character))) and (-end_cursor < length):
            end_cursor -= 1
        if -end_cursor >= length:
            break
        character = ffs[end_cursor]
        ec2 = end_cursor
        while ffs[ec2] == character:
            ec2 -= 1
        character_count = end_cursor - ec2

        # Find the next empty block
        i = 0
        while i <= ec2:
            free_space = 0
            while ffs[i] != '.':
                i += 1
                if i > ec2:
                    break
            while ffs[i] == '.':
                free_space += 1
                i += 1
                if i > ec2:
                    break
                if free_space == character_count:
                    break
            if free_space < character_count:
                continue
            else:
                break
        if free_space == character_count:
            for j in range(character_count):
                ffs[i - free_space + j], ffs[ec2 + j + 1] = ffs[ec2 + j + 1], ffs[i - free_space + j]
        else:
            ignore.append(character)
    checksum = 0
    i = 0
    while i < length:
        # print(f"{i} / {length}")
        if ffs[i] != '.':
            checksum += i * int(ffs[i])
        i += 1
    print("Part 2: ", checksum)