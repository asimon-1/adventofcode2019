from utils import get_input, run_main
from itertools import product


def addition(intcode, pointer, mode1, mode2, mode3):
    param1 = intcode[pointer + 1]
    param2 = intcode[pointer + 2]
    param3 = intcode[pointer + 3]
    val1 = param1 if mode1 else intcode[param1]
    val2 = param2 if mode2 else intcode[param2]

    if mode3:
        # Immediate
        raise RuntimeError
    else:
        # Position
        intcode[param3] = val1 + val2
    return intcode, pointer + 4


def multiplication(intcode, pointer, mode1, mode2, mode3):
    param1 = intcode[pointer + 1]
    param2 = intcode[pointer + 2]
    param3 = intcode[pointer + 3]
    val1 = param1 if mode1 else intcode[param1]
    val2 = param2 if mode2 else intcode[param2]
    if mode3:
        # Immediate
        raise RuntimeError
    else:
        # Position
        intcode[param3] = val1 * val2
    return intcode, pointer + 4


def input(intcode, pointer, inp):
    param1 = intcode[pointer + 1]
    intcode[param1] = inp
    return intcode, pointer + 2


def output(intcode, pointer, mode1):
    param1 = intcode[pointer + 1]
    return intcode, pointer + 2, (param1 if mode1 else intcode[param1])


def jump_if_true(intcode, pointer, mode1, mode2):
    param1 = intcode[pointer + 1]
    param2 = intcode[pointer + 2]
    val1 = param1 if mode1 else intcode[param1]
    val2 = param2 if mode2 else intcode[param2]
    return intcode, (val2 if val1 else pointer + 3)


def jump_if_false(intcode, pointer, mode1, mode2):
    param1 = intcode[pointer + 1]
    param2 = intcode[pointer + 2]
    val1 = param1 if mode1 else intcode[param1]
    val2 = param2 if mode2 else intcode[param2]
    return intcode, (val2 if not val1 else pointer + 3)


def less_than(intcode, pointer, mode1, mode2):
    param1 = intcode[pointer + 1]
    param2 = intcode[pointer + 2]
    param3 = intcode[pointer + 3]
    val1 = param1 if mode1 else intcode[param1]
    val2 = param2 if mode2 else intcode[param2]
    if val1 < val2:
        intcode[param3] = 1
    else:
        intcode[param3] = 0
    return intcode, pointer + 4


def equal(intcode, pointer, mode1, mode2):
    param1 = intcode[pointer + 1]
    param2 = intcode[pointer + 2]
    param3 = intcode[pointer + 3]
    val1 = param1 if mode1 else intcode[param1]
    val2 = param2 if mode2 else intcode[param2]
    if val1 == val2:
        intcode[param3] = 1
    else:
        intcode[param3] = 0
    return intcode, pointer + 4


def run_opcode(intcode, inp):
    intcode = intcode.copy()
    pointer = 0
    out = 0
    opcode = intcode[pointer]

    # Run the intcode
    while (operation := opcode % 100) != 99:
        mode1 = opcode // 10 ** 2 % 10
        mode2 = opcode // 10 ** 3 % 10
        mode3 = opcode // 10 ** 4 % 10
        if operation == 1:
            # Addition
            intcode, pointer = addition(intcode, pointer, mode1, mode2, mode3)
        elif operation == 2:
            # Multiplication
            intcode, pointer = multiplication(intcode, pointer, mode1, mode2, mode3)
        elif operation == 3:
            # Input
            intcode, pointer = input(intcode, pointer, inp)
        elif operation == 4:
            # Output
            intcode, pointer, out = output(intcode, pointer, mode1)
        elif operation == 5:
            # Jump-if-true
            intcode, pointer = jump_if_true(intcode, pointer, mode1, mode2)
        elif operation == 6:
            # Jump if false
            intcode, pointer = jump_if_false(intcode, pointer, mode1, mode2)
        elif operation == 7:
            # Less than
            intcode, pointer = less_than(intcode, pointer, mode1, mode2)
        elif operation == 8:
            # Equals
            intcode, pointer = equal(intcode, pointer, mode1, mode2)

        opcode = intcode[pointer]

    return out


def main(directory, test=False, part_2=False):
    input_text = get_input(directory)
    if test:
        if not part_2:
            original_intcode = [int(x) for x in input_text.splitlines()[0].split(",")]
        else:
            original_intcode = [int(x) for x in input_text.splitlines()[1].split(",")]
    else:
        original_intcode = [int(x) for x in input_text.split(",")]

    if not part_2:
        inp = 1
    else:
        if test:
            inp = 8
        else:
            inp = 5

    return run_opcode(original_intcode, inp)


if __name__ == "__main__":
    run_main(main)
