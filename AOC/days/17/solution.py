from pathlib import Path

data = open(Path(Path(__file__).parent, "input"), "r").readlines()

A = int(data[0].strip().split(": ")[1])
B = int(data[1].strip().split(": ")[1])
C = int(data[2].strip().split(": ")[1])

program = [int(x) for x in data[4].strip().split(":")[1].strip().split(",")]
"""
Combo operands 0 through 3 represent literal values 0 through 3.
Combo operand 4 represents the value of register A.
Combo operand 5 represents the value of register B.
Combo operand 6 represents the value of register C.
Combo operand 7 is reserved and will not appear in valid programs.
"""


def combo(literal: int) -> int:
    """
    convert literal operand to its combo value
    """
    global A
    global B
    global C
    match literal:
        case 0 | 1 | 2 | 3:
            return literal
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case _:
            raise ValueError("Invalid combo operand")


output = ""


def adv(literal: int) -> None:
    """
    Divide A by 2^(combo operand) and truncate to integer
    """
    global A
    global pointer
    pointer += 2
    A //= 2 ** combo(literal)


def bxl(literal: int):
    """
    Calculate the bitwise XOR of B and the literal operand and store the result in B
    """
    global B
    global pointer
    pointer += 2
    B ^= literal


def bst(literal: int):
    """
    write the value of the combo operand modulo 8 to the B register
    """
    global B
    global pointer
    B = combo(literal) % 8
    pointer += 2


def jnz(literal: int):
    """
    do nothing if A is zero, else move pointer to value of literal operand
    of it jumps, do not increment pointer as usual
    """
    global pointer
    if A == 0:
        pointer += 2
        return
    pointer = literal


def bxc(literal: int):
    """
    Calculate bitwise XOR of B and C and store the result in B
    """
    global B
    global C
    global pointer
    pointer += 2
    B ^= C


def out(literal: int):
    """
    output the value of the combo operand modulo 8, seperate characters with a comma
    """
    global output
    global pointer
    pointer += 2
    if output:
        output += ","
    output += ",".join(list(str(combo(literal) % 8)))


def bdv(literal: int) -> None:
    """
    Divide A by 2^(combo operand) and truncate to integer, store in B
    """
    global A
    global B
    global pointer
    pointer += 2
    B = A // 2 ** combo(literal)


def cdv(literal: int) -> None:
    """
    Divide A by 2^(combo operand) and truncate to integer, store in C
    """
    global A
    global C
    global pointer
    pointer += 2
    C = A // 2 ** combo(literal)


def operation(opcode: int, literal: int) -> None:
    """
    Perform operation based on opcode
    """
    match opcode:
        case 0:
            adv(literal)
        case 1:
            bxl(literal)
        case 2:
            bst(literal)
        case 3:
            jnz(literal)
        case 4:
            bxc(literal)
        case 5:
            out(literal)
        case 6:
            bdv(literal)
        case 7:
            cdv(literal)
        case _:
            raise ValueError("Invalid opcode")


pointer = 0

if __name__ == "__main__":
    i = 0
    while output != program:
        output = ""
        pointer = 0
        i += 8
        A = i
        if A % 10000 == 0:
            print(A)
        while pointer < len(program):
            opcode, literal = program[pointer], program[pointer + 1]
            operation(opcode, literal)
    print(A)


# 760290000
# 198100000
